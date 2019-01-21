# [Credit Card Default Predicting Model](http://www.aboringwebsite.com/presentation?transition=concave#)
 
We are using the consumer data provided by [UCI Engineering Department](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients) to create a credit card default prediction model. The population is over 30,000.There are 24 variables, including age, sex, education and etc. We use the dataset to train 4 regression models and predict if a new customer would default or not.

## last updated

01-02-2019

## Preview

**[the Presentation Mode](http://www.aboringwebsite.com/presentation?transition=concave#)**
[![Wesbite Preview](static/img/website_preview.png)](http://www.aboringwebsite.com/)

## Project folder structure

### project_credit_card_prediction

- static
  - css
  - js
  - img
  - json
  - scss
  - lib
  - node_modules
  - vendor
  - favicon.ico
- templates
  - index.html (main page)
  - sides_deck.html
  - visuals.html (visualization html to show additional charts)
- env.example (an example to set up environment to connect to AWS mySQL DB)
- app.py (main python file)
- core_ML_logic.py (core prediction model)
- upload_csv_to_mysql_script.py (run this file to set up a local or remote data table in MySQL database)
- requirements.txt: list out all necessary libraries/dependencies for the project
- README.md

## Libraries

- Core machine learning library: [sklearn](https://scikit-learn.org/stable/)
- Python libraries: Pandas, collections, pymysql
- HTML: [Bootstrap](https://getbootstrap.com/)
- JavaScript libraries: jQuery, reveal.js, d3.js, plotly.js
- Web framework: [Flask](http://flask.pocoo.org/)

## Server Environment

- Amazon Elastic Beanstalk

We used Elastic Beanstalk ito deploy our codes without worrying about the infrastructure. The Elastic Beanstalk environment will automatically set up the EC2 instance, VPC, and handle loan blancing, scaling and etc. You can find more information at Amazon Web Service Elastic Beanstalk webiste(https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)

## Deployment

### 1. How to run the code on your local computer

Make sure that you have the python 3 or above installed on your laptop. Your laptop could be either a PC or Mac.

- create a virtual environment (optional). let's say the virtual environment's name is "creditcardproject". `virtualenv creditcardproject` (optional)
- activate the virtualevn `source creditcardproject/bin/activate` (optional)
- clone the github repository `git@github.com:zjgcainiao/ML_CreditCardDefaultPrediction.git`
- on the terminal (Mac OS), navigate to the current project folder. it should look like `xxx-MacBook-Pro:ML_CreditCardDefaultPrediction:(username)$:`.
- install libraries `pip install -r requirements.txt`
- create a mysql database locally or remotely.
- make a copy of `.env.example` rename it to `.env`.
- modify the parameters in the `.env` file based on the database configuration.
- create the data table in Mysql DB by typing in the terminal `python upload_csv_to_mysql_scripts.py`
- create mysql table using create_mysql_table.sql
- the data is located at static/csv/cleaned_creditcard.csv
- after connecting the database, using the database varibales from the real .env setup (Slack channel fpg4 group)
- run the command on a terminal `flask run` or `python app.py`
- visit the http://127.0.0.1:5000/
- visit the site in the presentation mode at: <http://127.0.0.1:5000/presentation?transition=concave#/>

## Regression Models

 We are using the data from [UCI Engineering Department](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients) to create a credit card default prediction model. There are 24 variables in our regression models. We use combined of 4 regression models:
- Logistic Regression Model
- Decision Tree model
- Random Forest Model
- Naive Bayees Model

## Next Step

Improve the prediction model by implying Netural Network models. 
Adjust parameters to improve the accuracy 

## Team

- [Stephen Wang](https://github.com/zjgcainiao)
- and contributors
  - Abula
  - Shanakay
  - Farai
  - Alexandra

## Copyright and License

Code released under the [MIT License](https://opensource.org/licenses/MIT)

Special Thank you to [Everett Griffiths](https://github.com/fireproofsocks) for inspiration.
