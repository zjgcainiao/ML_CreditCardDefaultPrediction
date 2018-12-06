# [Credit Card Default Predicting Model (presentation mode)](http://fpg4finalproject-env.uyjerqqha9.us-west-2.elasticbeanstalk.com/presentation?transition=concave#)
 
We are using the data from [UCI Engineering Department](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients) to create a credit card default prediction model. There are 24 variables in our regression models. 

## last updated

12-01-2018

## Preview

**[View in the Presentation Mode](http://fpg4finalproject-env.uyjerqqha9.us-west-2.elasticbeanstalk.com/presentation?transition=concave#)**
or Go to the [website](http://fpg4finalproject-env.uyjerqqha9.us-west-2.elasticbeanstalk.com/)

[![Wesbite Preview](static/img/website_preview.png)](http://fpg4finalproject-env.uyjerqqha9.us-west-2.elasticbeanstalk.com/)

## Project folder structure

### project_credit_card_prediction

- core_ML_jupyter_notebook(jupyter notebook workplace)
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
- create_mysql_table.sql (run this file to set up a local or remote data table in mySQL )
- requirements.txt: list out all necessary libraries/dependanceis for the project
- readme.md

## libararies

- Core Machine Learning Library: sklearn
- Python libraries: pandas, collections,flask
- HTML: bootstrap
- Javascript: jQuery, reveal.js, d3.js, plotly.js
- Flask based application
- Amazon Elatic Beanstalk

## Deployment

### How to run the code locally

- create a virtual environment (optional). let's say the virtual environment's name is "finalproject". `virtualenv finalproject` (optional)
- activate the virtualevn `source finalproject/bin/activate` (optional)
- clone the gitlba repository `git@usc.bootcampcontent.com:fireproofsocks/fpg4.git`
- install libraries `pip install -r requirements.txt`
- create mysql table using create_mysql_table.sql
- the data is located at static/csv/cleaned_creditcard.csv
- after connecting the database, using the database varibales from the real .env setup (Slack channel fpg4 group)
- run the command on a terminal `flask run` or `python app.py`
- visit the http://127.0.0.1:5000/

## regression models

 We are using the data from [UCI Engineering Department](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients) to create a credit card default prediction model. There are 24 variables in our regression models. We use combined of 4 regression models:
- logistic regression model
- decision tree model
- Random Forest model
- Naive Bayees model

## Team

- [Stephen Wang](https://github.com/zjgcainiao)
- and contributors

## Copyright and License

Code released under the [MIT License](https://opensource.org/licenses/MIT)


Special Thank you to [Everett Griffiths](https://github.com/fireproofsocks) for inspiration.
