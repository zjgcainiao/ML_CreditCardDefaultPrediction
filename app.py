
# from dotenv import load_dotenv

import numpy as np
import pandas as pd
import os
#import sqlalchemy
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import text, desc
from sqlalchemy import create_engine, func
from flask import render_template
from flask import Flask, jsonify,request
import pymysql
from collections import OrderedDict
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text
from core_ML_logic import customer_prediction_func



#################################################
# Flask Setup
#################################################
application = Flask(__name__, static_folder='./static', static_url_path='')
# to make it work with AWS Elastic Beans
app=application



prefix=os.getenv("DATABASE_PREFIX")
host=os.getenv("DATABASE_HOST")
user=os.getenv("DATABASE_USERNAME")
password=os.getenv("DATABASE_PASSWORD")
port=int(os.getenv("DATABASE_PORT"))
db=os.getenv("DATABASE_NAME")

connection = pymysql.connect(host=host, user=user, passwd=password, db=db, port=port, cursorclass=pymysql.cursors.DictCursor)

# Establish cursor. NOTE: This will be used to perform SQL queries (even in raw query form!)
cursor = connection.cursor(pymysql.cursors.DictCursor)


#################################################
# Flask Routes
#################################################

@app.route("/", methods=['GET', 'POST'])
def welcome():
    # input_dataset_path='cleaned_creditcard.json'
    prediction_result=''
    prediction_section_title=''
    if request.method=='POST': 
        age=request.form.get('age')
        if age=='':
            age=29
        cc_limit_balance=int(float(request.form.get('cc_limit_balance'))) or 3000
        gender=int(float(request.form['gender'])) or 1
        education=int(float(request.form['education']))
        if education==1:
            grad_school=0
            university=0
            hight_school=1
        elif education==2:
            grad_school=0
            university=1
            hight_school=0
        else:
            grad_school=0
            university=9
            hight_school=1
        ismarried=request.form['ismarried'] or 1
        avg_bill_amt=float(request.form['avg_bill_amt']) or 2000
        avg_pay_amt=float(request.form['avg_pay_amt']) or 2000
        repayment_status=request.form['repayment_status']  or -1


        # assume the avg_bill_amt equals the bill_amt_5 to bill_amt6
        new_customer = OrderedDict([('limit_bal', cc_limit_balance), ('age', age), ('bill_amt1', avg_bill_amt),
        ('bill_amt2', avg_bill_amt), ('bill_amt3', avg_bill_amt), ('bill_amt4', avg_bill_amt),
        ('bill_amt5', avg_bill_amt), ('bill_amt6', avg_bill_amt), ('pay_amt1', avg_pay_amt),('pay_amt2', avg_pay_amt),
        ('pay_amt3', avg_pay_amt), ('pay_amt4', avg_pay_amt), ('pay_amt5',avg_pay_amt), ('pay_amt6', avg_pay_amt),
        ('male', gender), ('grad_school', grad_school), ('university', university), ('hight_school', hight_school),
        ('married', ismarried), ('pay_1', repayment_status), ('pay_2', repayment_status), ('pay_3', repayment_status),
        ('pay_4', repayment_status), ('pay_5', repayment_status), ('pay_6', repayment_status)])

        new_customer_series = pd.Series(new_customer)
        prediction_result=customer_prediction_func(new_customer_series)
        prediction_section_title='The Prediction Result'
    
    return render_template('index.html',prediction_result=prediction_result, prediction_section_title=prediction_section_title)

@app.route('/visuals')
def visuals():
    return render_template('visuals.html') 
@app.route("/presentation")
def reveal_demo():
    return render_template('slides_deck.html')



#HYPOTHESIS 1: Men are more likely to experience a credit card default than women"(Pie Chart)
@app.route('/default/bygender')
def default_gender():

    results = []
    cursor.execute("SELECT male, COUNT(male) as total_num_CC_default FROM CreditCardDefault.credit_card_tbl WHERE cc_default=1 GROUP BY male")
    print('Description: ', cursor.description)
    for row in cursor:
        print(row)
        results.append(row)
    # cursor.close()
    # connection.close()
    return jsonify(results)

#HYPOTHESIS 2: Age plays a factor in the amount of credit granted to an individual x-"age", y-"average credit amount granted"(Bubble Chart)
@app.route('/api/age_bal')
def delaycc():
    connection = pymysql.connect(host=host, user=user, passwd=password, db=db, port=port, cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    results = []
    cursor.execute("SELECT age, avg(limit_bal) as avg_credit_granted FROM CreditCardDefault.credit_card_tbl GROUP BY age")   
    print('Description: ', cursor.description)
    for row in cursor:
        print(row)
        results.append(row)
    # cursor.close()
    # connection.close()
    return jsonify(results)


# HYPOTHESIS 3: Younger people are most like to experience a credit card default x-"age group", y-"number of accounts"(Bubble Chart)
@app.route('/api/age_bal')
def agecc():
    connection = pymysql.connect(host=host, user=user, passwd=password, db=db, port=port, cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    results = []
    cursor.execute("SELECT age, avg(limit_bal) as avg_credit_granted FROM CreditCardDefault.credit_card_tbl GROUP BY age")   
    print('Description: ', cursor.description)
    for row in cursor:
        print(row)
        results.append(row)
    # cursor.close()
    # connection.close()
    return jsonify(results)    



@app.route('/population/summary')
def population():
    connection = pymysql.connect(host=host, user=user, passwd=password, db=db, port=port, cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    results = []
    cursor.execute("select age, count(*) as number_of_records from CreditCardDefault.credit_card_tbl group by age")
    for row in cursor:
        print(row)
        results.append(row)
    # cursor.close()
    # connection.close()
    return jsonify(results)     

@app.route('/default/sept_delays')
def september():
    connection = pymysql.connect(host=host, user=user, passwd=password, db=db, port=port, cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    results = []
    cursor.execute("select pay_1 as months_delayed_since_Sept,count(pay_1) as number_of_accounts from CreditCardDefault.credit_card_tbl where pay_1>0 group by pay_1")
    for row in cursor:
        print(row)
        results.append(row)
    # cursor.close()
    # connection.close()
    return jsonify(results)      
    
@app.route('/bill/payment')
def billpayment():
    connection = pymysql.connect(host=host, user=user, passwd=password, db=db, port=port, cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    results = []
    cursor.execute("select sum(bill_amt1) as a_Sept, sum(bill_amt2) as b_Aug,sum(bill_amt3) as c_July,sum(bill_amt4) as d_June,sum(bill_amt5) as e_May,sum(bill_amt6) as f_April,sum(pay_amt1) as g_Sept,sum(pay_amt2) as h_Aug,sum(pay_amt3) as i_July,sum(pay_amt4) as j_June,sum(pay_amt5) as k_May,sum(pay_amt6) as l_April from CreditCardDefault.credit_card_tbl")
    for row in cursor:
        print(row)
        results.append(row)
    # cursor.close()
    # connection.close()
    return jsonify(results)    

    # cursor.close()
    # connection.close()


   
if __name__ == '__main__':
    app.run(debug=True)
