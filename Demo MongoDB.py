#Demo MongoDB
import pymongo

#Connect
connectstring = "mongodb+srv://Zoozoo7:<password>@cluster0.avxht.mongodb.net/myFirstDatabase?retryWrites=true&w=majority, --tlsAllowInvalidCertificates"
myclient = pymongo.MongoClient(connectstring)

#Create
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#Create a new document
#mycol.insert_one({"-id":101, "company": "KEA", "contact":"Tue Hellster"})
#mycol.insert_one({"-id":102, "company": "BEIT", "contact":"Tue Hellster"})
#mycol.insert_one({"-id":103, "company": "bnnb", "contact":"Tue Hellster"})
#mycol.insert_one({"-id":103, "company": "bnnb", "contact":"Tue Hellster", "country":"DK"})

#Find/Show/Print
#Find All
for x in mycol.find():
    print(x)

# "Select" columns
#Exlude last name and id
#for c in mycol.find({}, {"-id":0, "company":0}):
#   print (x)

#Update One - Only first one
myquery = {"company":"KEA"}
newvalues = {"$set": {"company":"New KEA"}}
mycol.update_one(myquery, newvalues)

#Drop Delecte collection
#mycol.drop()
