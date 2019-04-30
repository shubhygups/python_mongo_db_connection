# Python Mongodb connection

## Description

Python program that reads from a json file, enters the data into MongoDB and performs on operations on the DB.

## Input

Input: a file "input.json" containing an array of product revenues (a sample input.json) is present in it.


Looking at input.json, creating a MongDB collection to hold the product details in a collection called "sales"

## Output

Program is first deleting all the items in "sales" collection. Next, it is reading input.json and insert all the elements into the
DB. Then, it is querying the DB and for each product, printing the top 3 countries with maximum total sales for that product.