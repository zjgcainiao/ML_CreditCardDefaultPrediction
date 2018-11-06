import pandas as pd
import numpy as np

from datetime import datetime
from sklearn import tree

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, confusion_matrix, precision_recall_curve, classification_report
from sklearn.preprocessing import RobustScaler
from sklearn.linear_model import LogisticRegression

def customer_prediction_func(new_data_orderedDict,input_dataset_path):
    # get the data from locally store json file 
    # the dataset is alo reside in the AWS mysql db. see .env file
    credit_default=pd.read_json(input_dataset_path)

    # Our dependent feature or target(respondent) variable will the `default` column (y)
    target_name = 'default'
    X= credit_default.drop('default', axis=1)
    #prepare our model - logistic regression
    roubust_scaler= RobustScaler()
    X= roubust_scaler.fit_transform(X)
    y= credit_default[target_name]
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.15, random_state=43, stratify=y)


    # Instance of the estimator
    logistic_regression = LogisticRegression(n_jobs=2, random_state =43)
    # train the estimator
    logistic_regression.fit(X_train, y_train)

    # Evalute the model
    y_pred_test = logistic_regression.predict(X_test)

    # Confusion matrix for the logistic regression
    # CM = confusion_matrix(y_pred=y_pred_test, y_true=y_test)
    # CMatrix(CM)

    data = new_data_orderedDict.values.reshape(1, -1)
    data = roubust_scaler.transform(data)
    prob = logistic_regression.predict_proba(data)[0][1]
    if prob >= 0.2:
        return 'Will default'
    else:
        return 'Will NOT Default'

# ----------------------------------------------------
# cnvert a string to number
def convertStr(s):
    """Convert string to either int or float."""
    try:
        ret = int(s)
    except ValueError:
        #Try float.
        ret = float(s)
    return ret
# -------------------End---------------------------------------
