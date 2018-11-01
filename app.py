
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


prefix=os.getenv("DATABASE_PREFIX")
host=os.getenv("DATABASE_HOST")
user=os.getenv("DATABASE_USERNAME")
password=os.getenv("DATABASE_PASSWORD")
port=int(os.getenv("DATABASE_PORT"))
db=os.getenv("DATABASE_NAME")

connection = pymysql.connect(host=host, user=user, passwd=password, db=db, port=port, cursorclass=pymysql.cursors.DictCursor)

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

# Establish cursor. NOTE: This will be used to perform SQL queries (even in raw query form!)
cursor = connection.cursor(pymysql.cursors.DictCursor)
# to make it work with AWS Elastic Beans
app=application
# app = Flask(__name__)
#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return render_template('index.html')

@app.route("/visuals")
def visuals():
    return render_template('visuals.html')    

@app.route("/default/bygender")
def default_gender():
    results = []
    cursor.execute("SELECT male, COUNT(male) as total_num_CC_default FROM CreditCardDefault.credit_card_tbl GROUP BY male")
    print('Description: ', cursor.description)
    for row in cursor:
        print(row)
        results.append(row)
    return jsonify(results)

    cursor.close()
    connection.close()

if __name__ == '__main__':
    app.run(debug=True)
