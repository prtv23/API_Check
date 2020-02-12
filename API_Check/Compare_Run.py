import Database_Query
import API_Put
import json

print (API_Put.Status)
API = str(API_Put.Status)

DB = Database_Query.var.replace("(u'", "")
DB1 = DB.replace("', )", "")
print (DB1)

if DB1 == API:
    print ("Success")

else:
    print ("Not Success")


