
import pandas as pd
dataset = pd.read_csv("Hotel.csv", index_col=0)

X= dataset.iloc[:;:].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,3] = labelencoder_x.fit_transform(X[:3])

Z = pd.DataFrame(X)

onehotencoder = OneHotEncoder(categorical_features=[3])
X = onehotencoder.fit_transform(X).toarray()




# Making Predictions with Data and Python : Predicting Credit Card Default | packtpub.com

# Data Preparation

default= pd.read_cvs("")
default.rename(columns=lambda x: x.lower(), inplace=True)
#Base values: Female, other_education, not_married
default['grad_school'] = (default['education']==1).astype('int')
default['university'] = (default['education']==2).astype('int')
default['high_school'] = (default['education']==3).astype('int')
default.drop('education', axis=1, inplace=True)

default['male'] = (default['sex']==1).astype('int')
default.drop('sex', axis=1, inplace=True)

default['married'] = (default['marriage']==1).astype('int')
default.drop('marriage', axis =1, inplace=True)

# for pay features if the `pay_` <= 0 then it means it was not delayed
pay_features = ['pay_1', 'pay_2', 'pay_3', 'pay_4', 'pay_5', 'pay_6']
for i in pay_features:
    default.loc[default[i]<=0, i] = 0
default.rename(columns={'default payment next month': 'default'}, inplace =True)

# import

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, confusion_matrix, precision_recall_curve
from sklearn.preprocessing import RobustScaler


traget_name = 'default'
X= default.drop('default', axis=1)
roubust_scaler= RobustScaler()
X= roubust_scaler.fit_transform(X)
y= default[traget_name]
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.15, random_state=123, stratify=y)


def CMatrix(CM, lables =['pay', 'default']):
    df = pd.DataFrame(data=CM, index=labels, columns=labels)
    df.index.name='True'
    df.columns.name="Prediction"
    df.loc["Total"] = df.sum()
    df['Total'] = df.sum(axis)
    return df

    # Preparing a DataFrame for Model Analysis

    #Data frame for evaluation metrics
    metrics = pd.DataFrame(index=['accuracy', 'percision', 'recall'],
                columns=['NULL', 'LogisticReg', 'ClassTree', 'NaiveBayes'])  

# The Null model: alwasys predict the most common category

y_pred_test = np.repeat(y_train_value_counts().indxmax(), y_test.size) 
metrics.loc['accuracy', 'NULL'] = accuracy_score(y_pred_test, y_true=y_test)
metrics.loc['precision', 'NULL'] = precisin_score(y_pred_test, y_true=y_test)
metrics.loc['recall', 'NULL'] = recall_score(y_pred_test, y_true=y_test)

CM = confusion_matrix(y_pred=y_pred_test, y_true=y_test)
CMatrix(CM)

A. Logistic Regression

#1. Import the estimator object (model)
from sklear.linear_model import LosisticRegression
#2. Create on Instance of the estimator
logistic_regress = LosisticRegression(n_jobs=-1, random_state =15)
#3. Use the trainning data to train the estimator
logistic_regression.fit(X_train, y_train)

#4. Evalute the model
y_pred_test = logistic_regression.redict(X_test)
merics.loc['accuracy', 'LogisticReg']= accuracy_score(y_pred=y_pred_test, y_true=Y_test)
merics.loc['precision', 'LogisticReg']= precision_score(y_pred=y_pred_test, y_true=Y_test)
merics.loc['recall', 'LogisticReg']= recall_score(y_pred=y_pred_test, y_true=Y_test)    

#Confusion matrix
CM = confusion_matrix(y_pred=y_pred_test, y_ture=y_test)
CMatrix(CM)

# B. Classification Trees

# 1. Import the estimator object (model)
from sklearn.tree import DecisionTreeClassifier
# 2.  Create on Instance of the estimator
class_tree = DecisionTreeClassifier(min_sample_split=30, min_samples_leaf=10, random_state=10)
# 3. Use the training data to train the estimator
class_tree.fit(X_train, y_train)
# 4. Evaluate the model

y_pred_test = class_tree.redict(X_test)
metrics.loc['accuracy', 'class_tree']= accuracy_score(y_pred=y_pred_test, y_true=Y_test)
metrics.loc['precision', 'class_tree']= precision_score(y_pred=y_pred_test, y_true=Y_test)
metrics.loc['recall', 'class_tree']= recall_score(y_pred=y_pred_test, y_true=Y_test)  
# Confussion matrix
CM = confusion_matrix(y_pred=y_pred, y_true=y_test)
CMatrix(CM)  

# C. Naive Bayes Classifier

# 1. Import the estimator object (model)
from sklearn.naive_bayes import GaussianNB
# 2.  Create on Instance of the estimator
NBC = GaussianNB()
# 3. Use the training data to train the estimator
NBC.fit(X_train, y_train)
# 4. Evaluate the model
y_pred_test = NBC.redict(X_test)
metrics.loc['accuracy', 'NaiveBayes']= accuracy_score(y_pred=y_pred_test, y_true=Y_test)
metrics.loc['precision', 'NaiveBayes']= precision_score(y_pred=y_pred_test, y_true=Y_test)
metrics.loc['recall', 'NaiveBayes']= recall_score(y_pred=y_pred_test, y_true=Y_test)  
# Confussion matrix
CM = confusion_matrix(y_pred=y_pred, y_true=y_test)
CMatrix(CM)  

fig, ax =plt.subplots(figsize=(8,5))
metrics.plot(kind='bar', ax=ax)
ax.grid();

# ---
precision_nb, recall_nb, threshold_nb= precision_recall_curvey(y_true_test, probas_pred=NBC.predict_proba(X_test)[:,1])
precision_lr, recall_lr, threshold_nb= precision_recall_curvey(y_true_test, probas_pred=logistic_regression.predict_proba(X_test)[:,1])
# ---
fig, ax = plt.subplots(figsize=(8,5))
ax.plot(precision_nb, recall_nb, label="NaiveBayes")
ax.plot(precision_lr, recall_lr, label="LogisticReg")
ax.set_xlabel('Precision')
ax.set_ylabel('Recall')
ax.set_title('Precision-Recall Curve')
#ax.hlines(y=0.5, xmin=0, xmax=1, color='red')
ax.legend()
ax.grid();

# Confusion matrix for modified Logistic Regression Classifier
fig, ax = plt.subplots(figsize=(8,5))
ax.plot(thresholds_lr, precision_lr[1:], label="Precision")
ax.plot(thresholds_nb, recall_lr, label="Recall")
ax.set_xlabel('Clasification Threshold')
ax.set_ylabel('Precision Recall')
ax.set_title('Logistic Regression Classifire: Precision_Recall')
ax.hlines(y=0.5, xmin=0, xmax=1, color='red')
ax.legend()
ax.grid();


# Classifier with threshold of 0.2
y_pred_proba = logistic_regression.predict_proba(X_test)[:,1]
y_pred_test = (y_pred_proba >= 0.2).astype('int')
# Confusion matrix
CM = confusion_matrix(y_pred=y_pred_test, y_true=y_test)
print("Recall: ", 100*recall_score(y_pred=y_pred_test, y_true=y_test))
print("Precision: ", 100*precision_score(y_pred=y_pred_test, y_true=y_test))
CMatrix(CM)

# Making Individual Predictions
def make_ind_prediction(new_data):
    data = new_data.values.reshape(1, -1)
    data = robust_scaler.transform(data)
    prob = logistic_regression.predict_proba(data)[0][1]
    if prob >= 0.2:
        return 'Will default'
    else:
        return 'Will pay'

    # ----
    pay = default[default['default']==0]
    # ---
    pay.head()
    # ---

    from collections import OrderedDict
    new_customer = OrderedDict([('limit_bal', 4000), ('age', 50), ('bill_amt1', 500),
    ('bill_amt2', 35509), ('bill_amt3', 689), ('bill_amt4', 0),
    ('bill_amt5', 0), ('bill_amt6', 0), ('pay_amt1', 0),('pay_amt2', 35509),
    ('pay_amt3', 0), ('pay_amt4', 0), ('pay_amt5', 0), ('pay_amt6', 0),
    ('male', 1), ('grad_school', 0), ('university', 1), ('hight_school', 0),
    ('married', 1), ('pay_1', -1), ('pay_2', -1), ('pay_3', -1),
    ('pay_4', 0), ('pay_5', -1), ('pay_6', 0)])

new_customer = pd.Series(new_customer)
make_ind_prediction(new_customer)
# -----

for x in negative.index[0:100]:
    print(make_ind_prediction(negative.loc[x].drop('default')))


