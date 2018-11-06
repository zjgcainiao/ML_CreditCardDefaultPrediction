
# from dotenv import load_dotenv
import numpy as np
import os
#import sqlalchemy
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import text, desc
from sqlalchemy import create_engine, func
from flask import render_template
from flask import Flask, jsonify
import pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text
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
<<<<<<< HEAD

=======
>>>>>>> 67c06262b3ae4abc1f2636942afe1d328b021c72

#################################################
# Flask Routes
#################################################

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/visuals')
def visuals():
    return render_template('visuals.html')    

<<<<<<< HEAD
#HYPOTHESIS 1: Men are more likely to experience a credit card default than women"(Pie Chart)
@app.route('/default/bygender')
def default_gender():
    connection = pymysql.connect(host=host, user=user, passwd=password, db=db, port=port, cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
=======
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
    
>>>>>>> 67c06262b3ae4abc1f2636942afe1d328b021c72
    results = []
    cursor.execute("SELECT male, COUNT(male) as total_num_CC_default FROM CreditCardDefault.credit_card_tbl WHERE cc_default=1 GROUP BY male")
    print('Description: ', cursor.description)
    for row in cursor:
        print(row)
        results.append(row)
    cursor.close()
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
    cursor.close()
    # connection.close()
    return jsonify(results)

<<<<<<< HEAD

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
    cursor.close()
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
    cursor.close()
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
    cursor.close()
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
    cursor.close()
    # connection.close()
    return jsonify(results)      
=======
    # cursor.close()
    # connection.close()
>>>>>>> 67c06262b3ae4abc1f2636942afe1d328b021c72

cursor.close()
connection.close()
   
if __name__ == '__main__':
    app.run(debug=True)
