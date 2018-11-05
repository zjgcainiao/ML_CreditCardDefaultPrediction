
# from dotenv import load_dotenv
import pandas as pd
import numpy as np
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
from core_ML_logic import customer_prediction_func,convertStr
# load_dotenv()


# reflect the tables
# Base.prepare(engine, reflect=True)

# # Save reference to the table
# Household_Income = Base.classes.household_income_by_state_us
# State_Revenue_Per_Capita=Base.classes.statesRevenue
# # Create our session (link) from Python to the DB
# session = Session(engine)

#################################################
# Flask Setup
#################################################
application = Flask(__name__, static_folder='./static', static_url_path='')
# to make it work with AWS Elastic Beans
app=application


## set up the connection between AWS mysql with pymsql
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
    input_dataset_path='cleaned_creditcard.json'
    prediction_result=''
    prediction_section_title=''
    if request.method=='POST':
        age=request.form.get('age')
        if age=='':
            age=29
        cc_limit_balance=int(float(request.form.get('cc_limit_balance')))
        gender=int(float(request.form['gender']))
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
        ismarried=request.form['ismarried']  
        avg_bill_amt=float(request.form['avg_bill_amt'])
        avg_pay_amt=float(request.form['avg_pay_amt'])
        repayment_status=request.form['repayment_status']    


        # assume the avg_bill_amt equals the bill_amt_5 to bill_amt6
        new_customer = OrderedDict([('limit_bal', cc_limit_balance), ('age', age), ('bill_amt1', avg_bill_amt),
        ('bill_amt2', avg_bill_amt), ('bill_amt3', avg_bill_amt), ('bill_amt4', avg_bill_amt),
        ('bill_amt5', avg_bill_amt), ('bill_amt6', avg_bill_amt), ('pay_amt1', avg_pay_amt),('pay_amt2', avg_pay_amt),
        ('pay_amt3', avg_pay_amt), ('pay_amt4', avg_pay_amt), ('pay_amt5',avg_pay_amt), ('pay_amt6', avg_pay_amt),
        ('male', ismarried), ('grad_school', grad_school), ('university', university), ('hight_school', hight_school),
        ('married', repayment_status), ('pay_1', repayment_status), ('pay_2', repayment_status), ('pay_3', repayment_status),
        ('pay_4', repayment_status), ('pay_5', repayment_status), ('pay_6', repayment_status)])

        new_customer_series = pd.Series(new_customer)
        prediction_result=customer_prediction_func(new_customer_series,input_dataset_path)
        prediction_section_title='The Prediction Result'
    
    return render_template('index.html',prediction_result=prediction_result, prediction_section_title=prediction_section_title)

@app.route("/visuals")
def visuals():
    return render_template('visuals.html')    

@app.route("/presentation")
def reveal_demo():
    return render_template('slides_deck.html')

@app.route("/api/gender")
def api_fetch_data():
    results=[]
    sql_script="SELECT count(id) as Counts, (case when male =0 then 'female' else 'male' end ) as 'gender' FROM CreditCardDefault.credit_card_tbl group by male"
    cursor.execute(sql_script)
    for row in cursor:
        results.append(row)
    return jsonify(results)

@app.route("/default/bygender")
def default_gender():
    
    results = []
    cursor.execute("SELECT male, COUNT(male) as total_num_CC_default FROM CreditCardDefault.credit_card_tbl GROUP BY male")
    print('Description: ', cursor.description)
    for row in cursor:
        print(row)
        results.append(row)
    return jsonify(results)

    # cursor.close()
    # connection.close()

@app.route('/#prediction', methods=['POST'])
def process_input_data():
    print(request.form)
    

        # prepare for the prediction

    new_customer = OrderedDict([('limit_bal', 4000), ('age', 50), ('bill_amt1', 500),
    ('bill_amt2', 35509), ('bill_amt3', 689), ('bill_amt4', 0),
    ('bill_amt5', 0), ('bill_amt6', 0), ('pay_amt1', 0),('pay_amt2', 35509),
    ('pay_amt3', 0), ('pay_amt4', 0), ('pay_amt5', 0), ('pay_amt6', 0),
    ('male', 1), ('grad_school', 0), ('university', 1), ('hight_school', 0),
    ('married', 1), ('pay_1', -1), ('pay_2', -1), ('pay_3', -1),
    ('pay_4', 0), ('pay_5', -1)
                                , ('pay_6', 0)])

    new_customer_series = pd.Series(new_customer)
    prediction_result=customer_prediction_func(new_customer)
    # age=+request.form['age']
    # your code
    # return a response
    # return 
    return render_template('index.html#prediction',prediction_result=prediction_result)

if __name__ == '__main__':
    app.run(debug=True)


