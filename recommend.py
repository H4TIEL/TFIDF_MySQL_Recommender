#Simple MySQL recommendation using TFIDF
import mysql.connector
import json
from tfidf import TfIdf
import nltk

table = TfIdf()
cnx = mysql.connector.connect(user='database_user', database='database_name')
cursor = cnx.cursor()
person = []
#text file containing personality traits
with open('personality.txt', 'r') as f:
    person = f.read()
    nltk_tokens = nltk.word_tokenize(person)

#example product_id,product_image and product_description as column names in product table
query = ("SELECT product_id,product_image,product_description FROM product")
cursor.execute(query)
for (product_id, product_image, product_description) in cursor:
    tempList = []
    for word in description.split(','):
        tempList.append(word)
        table.add_document(id, tempList)

result = table.similarities(nltk_tokens)
product_id = None
product_score = 0.0
for i in range(len(result)):
   if(result[i][1] > product_score):
        product_id = result[i][0]
        product_score = result[i][1]

#Default product_id if no recommendation
if(product_id == None):
    product_id = product_id
query2 = ("SELECT product_id,product_image FROM product WHERE id = "+str(product_id))
cursor.execute(query2)
for(id, image_path) in cursor:
    print(image_path)

cursor.close()
cnx.close()
