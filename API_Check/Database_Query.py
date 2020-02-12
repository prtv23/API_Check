import responses
import pyodbc
import PropertyFile

connection = pyodbc.connect(PropertyFile.getValue('DataBase','psmi'))
query = connection.cursor()
print ("Connected")

def DB_Connect(Query):
    Id = query.execute(Query)
    for record in Id:
        var = record[0]
        return var

