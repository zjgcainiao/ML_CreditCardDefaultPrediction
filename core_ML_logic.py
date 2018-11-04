
# coding: utf-8

# # Predicting the Default Rate for Credit Card Application

# ## The goal of this project is to show how to predict default on borrowing from the banks by using statistical `exploratory data analysis`, `machine learning` and `deep learning`. 

# ** *------------------------------------------------------------* **
# # Import some Libraries 

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn import tree

from matplotlib import pyplot as plt
import seaborn as sns

import graphviz
import pydotplus
import io
from scipy import misc

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, confusion_matrix, precision_recall_curve, classification_report
from sklearn.preprocessing import RobustScaler

import os     
os.environ["PATH"] += os.pathsep + 'C:/Users/abulla/Anaconda3/Lib/site-packages/graphviz/'
from sklearn.tree import export_graphviz
get_ipython().run_line_magic('matplotlib', 'inline')


# ---------------------------------------



df.columns = [x.lower() for x in df.columns]
credit_default = df.rename(index=str, columns={"pay_0": "pay_1"})
credit_default = credit_default.drop('id', axis=1)
credit_default.columns


# In[5]:


credit_default.head()


# # Attribute Information:
# ### 23 variables as explanatory variables: PLEASE Double Click on the Table to read the Markdown clearly.
# 
# |-----------------------------|-------------------------------------------------------------|
# | Variables                   | Description                                                 |
# |-----------------------------|-------------------------------------------------------------|
# | Yes = 1, No = 0             | default payment                                             |
# |-----------------------------|-------------------------------------------------------------|
# | limit_bal (X1)              | Amount of the given credit (NT dollar):                     |
# |                             |   it includes both the individual consumer credit and       |
# |                             |   his/her family (supplementary) credit.                    |
# |-----------------------------|-------------------------------------------------------------|
# | sex (X2)                    | 1 = male; 2 = female                                        |
# |-----------------------------|-------------------------------------------------------------|
# | education (X3)              | 1 = graduate school; 2 = university;                        | 
# |                             | 3 = high school; 4 = others                                 |
# |-----------------------------|-------------------------------------------------------------|
# | marriage (X4)               | 1 = married; 2 = single; 3 = others                         |
# |-----------------------------|-------------------------------------------------------------|
# | age (X5)                    | year                                                        |
# |-----------------------------|-------------------------------------------------------------|
# | pay_1 - pay_6               | History of past payment.                                    |
# |   (X6 - X11)                |  X6 = the repayment status in September, 2005;              |
# |                             |  X7 = the repayment status in August, 2005; . . .;          | |                             |  X11 = the repayment status in April, 2005.                 |
# |                             | The measurement scale for the repayment status is:          | |                             |   -1 = pay duly; 1 = payment delay for one month;           |
# |                             |    2 = payment delay for two months; . . .;                 |
# |                             |    8 = payment delay for eight months;                      |
# |                             |    9 = payment delay for nine months and above.             |
# |-----------------------------|-------------------------------------------------------------|
# | bill_amt1 - bill_amt6       | Amount of bill statement (NT dollar).                       | |   (X12 -X17)                |  X12 = amount of bill statement in September, 2005;         |
# |                             |  X13 = amount of bill statement in August, 2005; . . .;     |
# |                             |  X17 = amount of bill statement in April, 2005.             |
# |-----------------------------|-------------------------------------------------------------|
# | pay_amt1 - pay_amt6         | Amount of previous payment (NT dollar).                     |
# |                             |  X18 = amount paid in September, 2005;                      | |                             |  X19 = amount paid in August, 2005; . . .;                  |
# |                             |  X23 = amount paid in April, 2005.                          |
# |-----------------------------|-------------------------------------------------------------|
# 

# ** Use info and describe() on fd**

# In[6]:

credit_default.info()


# ---------------------------------------------

# ##  Data Preprocessing

# In[7]:


# Transform some attributes such as female, other_education, not_married
# Use n-1 rull.
credit_default['grad_school'] = (credit_default['education']==1).astype('int')
credit_default['university'] = (credit_default['education']==2).astype('int')
credit_default['high_school'] = (credit_default['education']==3).astype('int')
credit_default.drop('education', axis=1, inplace=True)


# In[8]:


credit_default['male'] = (credit_default['sex']==1).astype('int')
credit_default.drop('sex', axis=1, inplace=True)

credit_default['married'] = (credit_default['marriage']==1).astype('int')
credit_default.drop('marriage', axis =1, inplace=True)


# In[9]:


#  if the `pay_features` <= 0 then it means it was not delayed
pay_features = ['pay_1', 'pay_2', 'pay_3', 'pay_4', 'pay_5', 'pay_6']
for j in pay_features:
    credit_default.loc[credit_default[j]<=0, j] = 0
credit_default.rename(columns={'default payment next month': 'default'}, inplace =True)


# In[10]:


# Visualize the transformed dataset
credit_default.head()


# In[11]:


credit_default.to_csv('cleaned_cerditcard.csv', sep = ',')


# # Some visualization
# 

# In[12]:


# import regex
import re


# In[13]:


pattern = re.compile("^pay_[0-9]+$")
payment_status = [ x for x in credit_default.columns if (pattern.match(x))]

fig, ax = plt.subplots(2,3)
fig.set_size_inches(15,5)
fig.suptitle('Distribution of dalays in the past 6 months')

for i in range(len(payment_status)):
    row,col = int(i/3), i%3

    d  = credit_default[payment_status[i]].value_counts()
    ax[row,col].bar(d.index, d, align='center', color='r')
    ax[row,col].set_title(payment_status[i])

plt.tight_layout(pad=3.0, w_pad=0.5, h_pad=1.0)
plt.show()


# In[14]:


# Payment status by Sex
male = credit_default[credit_default['default']==1]['male']
female = credit_default[credit_default['default']==0]['male']

fig = plt.figure(figsize = (9,5))
plt.title("Payment status by Sex")
female.hist(color="green", alpha=0.7, bins = 30, label="Female")
male.hist(color="red", alpha=0.7, bins = 30, label="Male" )
plt.legend(loc="upper center")


# In[15]:


# pay status columns
pattern = re.compile("^pay_amt[0-9]+$")
pay_amount_columns = [ x for x in df.columns if (pattern.match(x))]
df[pay_amount_columns].describe()


# In[16]:


# Let make pairplot using seaborn
plt.figure(figsize=(11,7))
sns.countplot(x='married',hue='default',data=credit_default,palette='Set1')


# # Model Specification

# ## Import the following for data processing

# ## Specify the Dependent and Independent Variables or features

# In[17]:


# Our dependent feature or target(respondent) variable will the `default` (y)
traget_name = 'default'


# In[18]:


# Our independent features or explantory variables (X)
X= credit_default.drop('default', axis=1)


# In[19]:


X.head()


# ### Let use roubust_scaler to transform our data to fit for the analysis

# In[20]:


roubust_scaler= RobustScaler()
X= roubust_scaler.fit_transform(X)
y= credit_default[traget_name]
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.15, random_state=123, stratify=y)


# ## Let define a common DataFrame for our Models analysis and comparisons

# 
# 
#      

# In[21]:


# DataFrame for our Models Analysis
def CMatrix(CM, labels =['non-default', 'default']):
    df = pd.DataFrame(data=CM, index=labels, columns=labels)
    df.index.name='True'
    df.columns.name="Prediction"
    df.loc["Total"] = df.sum()
    df['Total'] = df.sum(axis=1)
    return df


# In[22]:


#Data frame for evaluation metrics for the models we are going to evaluate
eval_metrix = pd.DataFrame(index=['accuracy', 'precision', 'recall'],
                columns=['LogisticReg', 'ClassTree', 'RandomForest','NaiveBayes'])


# In[23]:


# Let view our empty dataframe
eval_metrix


# ## 1. Logistic Regression

# ### Follow the 5 main steps in Model Dev't in ML
# 
# * import the estimator object
# * Create on Instance of the estimator
# * Use the trainning data to train the estimator
# * Evalute the model
# * print out Confusion matrix using CM we have defined earlier
# 
# 

# In[24]:



# Import
from sklearn.linear_model import LogisticRegression
# Instance of the estimator
logistic_regression = LogisticRegression(n_jobs=-1, random_state =15)
# train the estimator
logistic_regression.fit(X_train, y_train)

# Evalute the model
y_pred_test = logistic_regression.predict(X_test)
# we conduct our evaluation using these 3 _score
eval_metrix.loc['accuracy', 'LogisticReg']= accuracy_score(y_pred=y_pred_test, y_true=y_test)
eval_metrix.loc['precision', 'LogisticReg']= precision_score(y_pred=y_pred_test, y_true=y_test)
eval_metrix.loc['recall', 'LogisticReg']= recall_score(y_pred=y_pred_test, y_true=y_test)    

# Confusion matrix for the logistic regression
CM = confusion_matrix(y_pred=y_pred_test, y_true=y_test)
CMatrix(CM)


# In[25]:


print(classification_report(y_test, y_pred_test))


# In[26]:


#Recall = TP/(TP + FN) => is a true positive rate
Recall = 324/(324+671)
Recall


# In[27]:


#Precision = TP/(TP + FP) => is a measure of accuracy
Precision = 324/(324+140)
Precision


# In[28]:


# f1_score = 2*(Precision*Recall)/(Precision + Recall)
f1_score = 2*(0.6982758620689655*0.3256281407035176)/(0.6982758620689655 + 0.3256281407035176)
f1_score


# ### Take the first row, and look the matrix.
# * For example `pay` by `pay` at Row 1 and Column 2:- shows the number of credit card holders who have been predicted by the logistic_regression model correctly as these who actually have paid their loan. 
# * By the same token, `pay` by `default`, row 1 and column 3, are these credit card holders who have been predicted by logistic_regression model to be `defaulter` while they actually paid their loan.

# ## 2. Decision Trees

# * import the estimator object
# * Create on Instance of the estimator
# * Use the trainning data to train the estimator
# * Evalute the model
# * print out Confusion matrix using CM we have defined earlier

# In[29]:



# Import 
from sklearn.tree import DecisionTreeClassifier

# Instance of the estimator
class_tree = DecisionTreeClassifier(min_samples_split=30, min_samples_leaf=10, random_state=10)

# train the estimator
class_tree.fit(X_train, y_train)

# Evaluate the model
y_pred_test = class_tree.predict(X_test)
# we conduct our evaluation using these 3 _score
eval_metrix.loc['accuracy', 'ClassTree']= accuracy_score(y_pred=y_pred_test, y_true=y_test)
eval_metrix.loc['precision', 'ClassTree']= precision_score(y_pred=y_pred_test, y_true=y_test)
eval_metrix.loc['recall', 'ClassTree']= recall_score(y_pred=y_pred_test, y_true=y_test)  

# Confussion matrix
CM = confusion_matrix(y_pred=y_pred_test, y_true=y_test)
CMatrix(CM)  


# In[30]:


print(classification_report(y_test, y_pred_test))


# In[31]:


#Recall = TP/(TP + FN) => is a true positive rate
Recall = 361/(361+634)
Recall


# In[64]:


#Precision = TP/(TP + FP) => is a measure of accuracy
Precision = 361/(361+320)
Precision


# In[33]:


# f1_score = 2*(Precision*Recall)/(Precision + Recall)
f1_score = 2*(0.5301027900146843*0.3628140703517588)/(0.5301027900146843 + 0.3628140703517588)
f1_score


# In[34]:


## Let print out our Trees


# In[35]:


independent_var = ['limit_bal', 'age', 'pay_1', 'pay_2', 'pay_3', 'pay_4', 'pay_5',
       'pay_6', 'bill_amt1', 'bill_amt2', 'bill_amt3', 'bill_amt4',
       'bill_amt5', 'bill_amt6', 'pay_amt1', 'pay_amt2', 'pay_amt3',
       'pay_amt4', 'pay_amt5', 'pay_amt6', 'grad_school',
       'university', 'high_school', 'male', 'married']


# In[65]:


import mglearn
get_ipython().run_line_magic('matplotlib', 'inline')
import graphviz
from sklearn.tree import export_graphviz

export_graphviz(class_tree, out_file="mytree.dot", feature_names=independent_var, class_names=['yes', 'no'], impurity=False, filled=True)



# ![](mytree.png)

# ## 3.  Random Forest model

# * import the estimator object
# * Create on Instance of the estimator
# * Use the trainning data to train the estimator
# * Evalute the model
# * print out Confusion matrix using CM we have defined earlier

# In[66]:


# Import 
from sklearn.ensemble import RandomForestClassifier

# Instance of the estimator
random_forest = RandomForestClassifier(n_estimators=20, random_state=10)

# train the estimator
random_forest.fit(X_train, y_train)

# Evaluate the model
y_pred_test = random_forest.predict(X_test)
# we conduct our evaluation using these 3 _score
eval_metrix.loc['accuracy', 'RandomForest']= accuracy_score(y_pred=y_pred_test, y_true=y_test)
eval_metrix.loc['precision', 'RandomForest']= precision_score(y_pred=y_pred_test, y_true=y_test)
eval_metrix.loc['recall', 'RandomForest']= recall_score(y_pred=y_pred_test, y_true=y_test)  

# Confussion matrix
CM = confusion_matrix(y_pred=y_pred_test, y_true=y_test)
CMatrix(CM)  


# In[67]:


print(classification_report(y_test, y_pred_test))


# In[39]:


#Recall = TP/(TP + FN) => is a true positive rate
Recall = 343/(343+ 652)
Recall


# In[40]:


#Precision = TP/(TP + FP) => is a measure of accuracy
Precision = 343/(342+189)
Precision


# In[41]:


# f1_score = 2*(Precision*Recall)/(Precision + Recall)
f1_score = 2*(0.6459510357815442*0.34472361809045227)/(0.6459510357815442 + 0.34472361809045227)
f1_score


# ## 3. Naive Bayes Classifier

# * import the estimator object
# * Create on Instance of the estimator
# * Use the trainning data to train the estimator
# * Evalute the model
# * print out Confusion matrix using CM we have defined earlier

# In[42]:



# Import 
from sklearn.naive_bayes import GaussianNB
# Instance of the estimator
NBC = GaussianNB()
# 3.  train the estimator
NBC.fit(X_train, y_train)
# Evaluate the model
y_pred_test = NBC.predict(X_test)
eval_metrix.loc['accuracy', 'NaiveBayes']= accuracy_score(y_pred=y_pred_test, y_true=y_test)
eval_metrix.loc['precision', 'NaiveBayes']= precision_score(y_pred=y_pred_test, y_true=y_test)
eval_metrix.loc['recall', 'NaiveBayes']= recall_score(y_pred=y_pred_test, y_true=y_test)  
# Confussion matrix
CM = confusion_matrix(y_pred=y_pred_test, y_true=y_test)
CMatrix(CM)  


# In[43]:


print(classification_report(y_test, y_pred_test))


# In[44]:


#Recall = TP/(TP + FN) => is a true positive rate
Recall = 556/(556+ 439)
Recall


# In[45]:


#Precision = TP/(TP + FP) => is a measure of accuracy
Precision = 556/(556+593)
Precision


# In[46]:


# f1_score = 2*(Precision*Recall)/(Precision + Recall)
f1_score = 2*(0.48389904264577893*0.5587939698492462)/(0.48389904264577893 + 0.5587939698492462)
f1_score


# ----------------------------

# In[47]:


# Evaluation Metrix for all the models

100*eval_metrix


# ----------------

# In[63]:


fig, ax=plt.subplots(figsize=(8,5))
eval_metrix.plot(kind='bar', ax=ax)
ax.grid();
fig.savefig('regression_modals.png')
ax.


# --------------------------------

# * we can see from the above graph that, 
#     * In terms of accurcy, the best model is LogisticReg
#     * In terms of prcision, the best model is LogisticReg
#     * In terms of recall, the best model is NaiveBayes
# * However we can improve the performance of our model by adjusting the values of precision and recall by modifying the classification thresholds.
# 
# * Here, our obective is to adjust the threshold level where LR will give a better recall than NaviveBayes.
# * We can use the `precision_recall_curve` to do this. This the role of supervisze learning in ML.

# ## Let now `supervise` our model by using `precision_recall_curve`

# In[49]:


precision_nb, recall_nb, thresholds_nb= precision_recall_curve(y_true=y_test, probas_pred=NBC.predict_proba(X_test)[:,1])
precision_lr, recall_lr, thresholds_lr= precision_recall_curve(y_true=y_test, probas_pred=logistic_regression.predict_proba(X_test)[:,1])


# In[50]:


# Now print out the Precision-Recall Curve to compare them
fig, ax = plt.subplots(figsize=(8,5))
ax.plot(precision_nb, recall_nb, label="NaiveBayes")
ax.plot(precision_lr, recall_lr, label="LogisticReg")
ax.set_xlabel('Precision')
ax.set_ylabel('Recall')
ax.set_title('Precision-Recall Curve')
ax.hlines(y=0.5, xmin=0, xmax=1, color='green')
ax.legend()
ax.grid();


# * We can see from the graph that at the recall value shown by the stright line, LogisticReg Model is higher value than NavieBayes model.
# * So Logistic is the better model to predict the default as compare to NaiveBayes
# * But,we need to 

# ## Confusion matrix for modified Logistic Regression Classifier

# In[51]:


fig, ax = plt.subplots(figsize=(8,5))
ax.plot(thresholds_lr, precision_lr[1:], label="Precision")
ax.plot(thresholds_lr, recall_lr[1:], label="Recall")
ax.set_xlabel('Clasification Threshold')
ax.set_ylabel('Precision Recall')
ax.set_title('Logistic Regression Classifire: Precision-Recall')
ax.hlines(y=0.6, xmin=0, xmax=1, color='pink')
ax.legend()
ax.grid();


# # From the above graph, we can see that we can adjust the Recall to be better that Percision by changing the classification threshold.
# ### Classifier with threshold of 0.2

# In[52]:


y_pred_proba = logistic_regression.predict_proba(X_test)[:,1]
y_pred_test = (y_pred_proba >= 0.2).astype('int')


# In[53]:


# Confusion matrix
CM = confusion_matrix(y_pred=y_pred_test, y_true=y_test)
print("Recall: ", 100*recall_score(y_pred=y_pred_test, y_true=y_test))
print("Precision: ", 100*precision_score(y_pred=y_pred_test, y_true=y_test))
CMatrix(CM)


# ### Take the first row, and look the matrix.
# * For example `pay` by `pay` at Row 1 and Column 2:- shows the number of credit card holders who have been predicted by the logistic_regression model correctly as these who actually have paid their loan. 
# * By the same token, `pay` by `default`, row 1 and column 3, are these credit card holders who have been predicted by logistic_regression model to be `defaulter` while they actually paid their loan.

# In[54]:


print(classification_report(y_test, y_pred_test))


# In[55]:


#Recall = TP/(TP + FP) => is a true positive rate
Recall = 592/(592+403)
Recall


# In[56]:


#Precision = TP/(TP + FP) => is a measure of accuracy
Precision = 592/(592+644)
Precision


# ## Let define a function for individual customer predictions using Logistic Regression¶

# In[57]:


def ind_customer_prediction(new_data):
    data = new_data.values.reshape(1, -1)
    data = roubust_scaler.transform(data)
    prob = logistic_regression.predict_proba(data)[0][1]
    if prob >= 0.2:
        return 'Will default'
    else:
        return 'Will pay'


# In[58]:


pay = credit_default[credit_default['default']==0]


# In[59]:


pay.head()


# In[60]:


from collections import OrderedDict

new_customer = OrderedDict([('limit_bal', 4000), ('age', 50), ('bill_amt1', 500),
('bill_amt2', 35509), ('bill_amt3', 689), ('bill_amt4', 0),
('bill_amt5', 0), ('bill_amt6', 0), ('pay_amt1', 0),('pay_amt2', 35509),
('pay_amt3', 0), ('pay_amt4', 0), ('pay_amt5', 0), ('pay_amt6', 0),
('male', 1), ('grad_school', 0), ('university', 1), ('hight_school', 0),
('married', 1), ('pay_1', -1), ('pay_2', -1), ('pay_3', -1),
('pay_4', 0), ('pay_5', -1)
                            , ('pay_6', 0)])

new_customer = pd.Series(new_customer)
ind_customer_prediction(new_customer)


# ----------------------------------------------------

# -------------------End---------------------------------------
