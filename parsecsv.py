# Import libraries
from dotenv import load_dotenv
import csv
import pymysql
import datetime
import os

load_dotenv()
#Connect to the database
prefix=os.getenv("DATABASE_PREFIX")
host=os.getenv("DATABASE_HOST")
user=os.getenv("DATABASE_USERNAME")
password=os.getenv("DATABASE_PASSWORD")
port=int(os.getenv("DATABASE_PORT"))
db=os.getenv("DATABASE_NAME")

connection = pymysql.connect(host=host, user=user, passwd=password, db=db, port=port, cursorclass=pymysql.cursors.DictCursor)

# Establish cursor. NOTE: This will be used to perform SQL queries (even in raw query form!)
cursor = connection.cursor(pymysql.cursors.DictCursor)

# Establish cursor
cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS credit_card_tbl')

create_table_query = """
CREATE TABLE `CreditCardDefault`.`credit_card_tbl` (
  `id` INT(11) unsigned NOT NULL AUTO_INCREMENT,
  `limit_bal` DOUBLE,
  `age` INT(11),
  `pay_1` INT(11),
  `pay_2` INT(11),
  `pay_3` INT(11),
  `pay_4` INT(11),
  `pay_5` INT(11),
  `pay_6` INT(11),
  `bill_amt1` DOUBLE,
  `bill_amt2` DOUBLE,
  `bill_amt3` DOUBLE,
  `bill_amt4` DOUBLE,
  `bill_amt5` DOUBLE,
  `bill_amt6` DOUBLE,
  `pay_amt1` INT(11),
  `pay_amt2` INT(11),
  `pay_amt3` INT(11),
  `pay_amt4` INT(11),
  `pay_amt5` INT(11),
  `pay_amt6` INT(11),
  `cc_default` INT(11),
  `grad_school` INT(11),
  `university` INT(11),
  `high_school` INT(11),
  `male` INT(11),
  `married` INT(11),
  PRIMARY KEY (`id`)
  )ENGINE = InnoDB DEFAULT CHARACTER SET = utf8 
"""

print("Creating database...")
cursor.execute(create_table_query)


# Read the csv file and reference it in the variable, csv_data
csv_data = csv.reader(open('cleaned_cerditcard.csv', newline=''))
next(csv_data, None)
# Print data to console
for row in csv_data:
  limit_bal= row[1]
  age = row[2]
  pay_1 = row[3]
  pay_2 = row[4]
  pay_3 = row[5]
  pay_4 = row[6]
  pay_5 = row[7]
  pay_6 = row[8]
  bill_amt1 = row[9]
  bill_amt2 = row[10]
  bill_amt3 = row[11]
  bill_amt4 = row[12]
  bill_amt5 = row[13]
  bill_amt6 = row[14]
  pay_amt1 = row[15]
  pay_amt2 = row[16]
  pay_amt3 = row[17]
  pay_amt4 = row[18]
  pay_amt5 = row[19]
  pay_amt6 = row[20]
  cc_default = row[21]
  grad_school = row[22]
  university = row[23]
  high_school = row[24]
  male = row[25]
  married = row[26]

	
	#try:
		#date_occurred = datetime.datetime.strptime(date_occurred, "%Y-%m-%d")
	#except ValueError:
	#	continue
  print(row)
  
  insert_statement = """INSERT INTO credit_card_tbl
(`limit_bal`, `age`, `pay_1`, `pay_2`, `pay_3`,`pay_4`, `pay_5`,`pay_6`,`bill_amt1`,`bill_amt2`,`bill_amt3`,`bill_amt4`,`bill_amt5`,`bill_amt6`,`pay_amt1`, `pay_amt2`,`pay_amt3`,`pay_amt4`,`pay_amt5`,`pay_amt6`, `cc_default`,`grad_school`, `university`, `high_school`, `male`, `married`)
VALUES
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""" % (limit_bal, age, pay_1, pay_2, pay_3,pay_4,pay_5,pay_6,bill_amt1,bill_amt2,bill_amt3,bill_amt4,bill_amt5,bill_amt6,pay_amt1, pay_amt2,pay_amt3,pay_amt4,pay_amt5,pay_amt6, default,grad_school,university,high_school,male,married)


#print(insert_statement)
  cursor.execute(insert_statement)

			 
		 
# close the connection to the database.
connection.commit()
cursor.close()
print ("Done")