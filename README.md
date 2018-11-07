# [Credit Card Default Predicting Model](http://fpg4finalproject-env.uyjerqqha9.us-west-2.elasticbeanstalk.com/)

 We are using the data from [placeholder](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients) to create a credit card defaultprediction model. There are 24 variables in our regression models. We use combined of 4 regression models:
** logistic regression model
** decision tree model
** Random Forest model
** Naive Bayees model

 11-05-2018

## Preview

[![Wesbite Preview](static/img/website_preview.png)](http://fpg4finalproject-env.uyjerqqha9.us-west-2.elasticbeanstalk.com/)

**[View Live Preview](http://fpg4finalproject-env.uyjerqqha9.us-west-2.elasticbeanstalk.com/)**
Go to the [presentation mode](http://fpg4finalproject-env.uyjerqqha9.us-west-2.elasticbeanstalk.com/?transition=concave#)

## Project folder structure

project_credit_card_prediction
--- default_of_credit_card (jupyter notebook workplace)
--- static
    --- css
    --- js
    --- img
    --- json
    --- scss
    --- lib
    --- node_modules
    --- vendor
    --- favicon.ico
--- templates
    --- index.html (main page)
    --- sides_deck.html
    -- visuals.html (visualization html to show additional charts)
--- env.example (an example to set up environment to connect to AWS mySQL DB)
--- app.py (main python file)
--- core_ML_logic.py (core prediction file)

--- requirements.txt: list out all necessary libraries/dependanceis for the project
--- readme.md

## libararies

* Core Machine Learning Library: sklearn
* Python libraries: pandas, collections,flask
* HTML: bootstrap
* Javascript: jQuery, reveal.js, d3.js, plotly.js
* Flask based application

## Deployment

### How to run the code locally

* create a virtual environment (optional). let's say the virtual environment's name is "finalproject". `virtualenv finalproject` (optional)
* activate the virtualevn `source finalproject/bin/activate` (optional)
* clone the gitlba repository `git@usc.bootcampcontent.com:fireproofsocks/fpg4.git`
* install libraries `pip freeze >> requirements.txt`
* create mysql table using create_mysql_table.sql'
* the data is located at static/csv/cleaned_creditcard.csv
* after connecting the database, using the database varibales from the real .env setup (Slack channel fpg4 group)
* run the command on a terminal `flask run` or `python app.py`
* visit the http://127.0.0.1:5000/

## Team

* Abulla Othow Othuw
* Alexandra Boonsook
* Farai Mungofa
* Shanakay Brandford
* Stephen Wang

## Copyright and License

Code released under the [MIT]
The template is based on the [style portfolio](https://blackrockdigital.github.io/startbootstrap-stylish-portfolio).

* https://startbootstrap.com
* https://twitter.com/SBootstrap
