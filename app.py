
from dotenv import load_dotenv
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


load_dotenv()
app = Flask(__name__, static_folder='./static', static_url_path='')

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

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/visuals')
def visuals():
    return render_template('visuals.html')    

@app.route('/default/bygender')
def default_gender():
    results = []
    cursor.execute("SELECT male, COUNT(male) as total_num_CC_default FROM CreditCardDefault.credit_card_tbl WHERE cc_default=0 GROUP BY male")
    print('Description: ', cursor.description)
    for row in cursor:
        print(row)
        results.append(row)
    return jsonify(results)
    cursor.close()
    connection.close()

    
   
@app.route('/default/april_delays')
def april():
    results = []
    cursor.execute("select pay_6 as months_delayed_since_April,count(pay_6) as number_of_accounts from CreditCardDefault.credit_card_tbl where cc_default = 0 group by pay_6")
    for row in cursor:
        print(row)
        results.append(row)
    return jsonify(results)
    cursor.close()
    connection.close()
  

@app.route('/default/may_delays')
def may():
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    results = []
    cursor.execute("select pay_5 as months_delayed_since_May,count(pay_5) as number_of_accounts from CreditCardDefault.credit_card_tbl where cc_default = 0 group by pay_5")
    for row in cursor:
        print(row)
        results.append(row)
    return jsonify(results)
    cursor.close()
    connection.close()

 




@app.route("/default/june_delays")
def june():
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    results = []
    cursor.execute("select pay_4 as months_delayed_since_June,count(pay_4) as number_of_accounts from CreditCardDefault.credit_card_tbl where cc_default = 0 group by pay_4")
    for row in cursor:
        print(row)
        results.append(row)
    return jsonify(results)
    cursor.close()
    connection.close()


@app.route("/default/july_delays")
def julydelays():
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    results = []
    cursor.execute("select pay_3 as months_delayed_since_July,count(pay_3) as number_of_accounts from CreditCardDefault.credit_card_tbl where cc_default = 0 group by pay_3")
    for row in cursor:
        print(row)
        results.append(row)
    return jsonify(results)
    cursor.close()
    connection.close()
    
    



@app.route("/default/aug_delays")
def august():
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    results = []
    cursor.execute("select pay_2 as months_delayed_since_Aug,count(pay_2) as number_of_accounts from CreditCardDefault.credit_card_tbl group by pay_2")
    for row in cursor:
        print(row)
        results.append(row)
    return jsonify(results)
    cursor.close()
    connection.close()
   
      

@app.route('/default/sept_delays')
def september():
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    results = []
    cursor.execute("select pay_1 as months_delayed_since_Sept,count(pay_1) as number_of_accounts from CreditCardDefault.credit_card_tbl where cc_default=0 group by pay_1")
    for row in cursor:
        print(row)
        results.append(row)
    return jsonify(results)  
    cursor.close()
    connection.close()

   


@app.route("/sum/delayPayment/byage")
def delaycc():
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    results = []
    cursor.execute("SELECT age, sum(limit_bal) as cc_limit,sum(pay_1)as Sept_AvgDelay, sum(pay_2) as Aug_avgDelay, sum(pay_3) as July_avgDelay,sum(pay_4)as June_avgDelay, sum(pay_5) as May_avgDelay, sum(pay_6) as April_AvgDeliquency FROM CreditCardDefault.credit_card_tbl GROUP BY age")   
    print('Description: ', cursor.description)
    for row in cursor:
        print(row)
        results.append(row)
    return jsonify(results)
    cursor.close()
    connection.close()

if __name__ == '__main__':
    app.run(debug=True)
