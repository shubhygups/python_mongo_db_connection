from pymongo import MongoClient   						# Importing Pymongo for connection with mongodb 
from pprint import pprint 							# Impoerting pprint for pretty print 
import json 									# Importing json for conversion of string to object
import sys									# Importins sys for exit on error

f= open("input.json","r")  							# Reading a json file.

fileContent = f.read()  							# Storing contents of file in variable
file_content = json.loads(fileContent) 						# Converting string to dict object
try:
	client=MongoClient()							# Trying to setup connection with mongodb database
	pprint("Connection successfully setup")					# Successful connection setup
except:
	pprint("Connection not setup")						# Connection setup fail
	sys.exit(1)								# Exiting with non-zero error code
	
	
db = client.any_db								# Database named as "any_db" and creating db as object of same database

db.sales.drop() # or db.sales.remove()						# Deleting all the documents in collection

col = db.sales									# Creating col as collection object

for key,int_dict in file_content.items():					# Inserting all the elements of input file in to collecction
	for item in int_dict:								
		col.insert_one(item)


distinct_prod=db.sales.distinct("prod")						# Query to get all distinct products

for value in distinct_prod:							# Loop over distinct products
	print("\n")
	pipeline=[								# Aggregate query to get top 3 countries with maximum total sales for each distinct product
		{"$match": {"prod": {"$in": [value]}}},
		{"$group": {"_id": {"prod":"$prod","country": "$country"}, "total_price": {"$sum": "$price"}}},
		{"$sort": {"total_price": -1,"prod":1}},
		{"$limit": 3}
	]
	docs=db.sales.aggregate(pipeline)					# Executing the query on collection

	for doc in docs:							# Printing top 3 top documents having maximum total sales for each product.
		pprint(doc)

	

