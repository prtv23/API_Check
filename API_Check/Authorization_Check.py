import requests
import json
import StatusCodes
import jsonpath
import grequests
import PropertyFile

# API URI
url = PropertyFile.getValue('URI','po_dispute')

# Read input json file
file = open(PropertyFile.getValue('JSON_PATH','po_dispute_json'),'r')
json_input = file.read()

# Convert the string from the input file into Json format
request_json = json.loads(json_input)
request_json_body = json.dumps(request_json)
print ("Request Json Body")
print (request_json_body)

# Make Post Request with Json Input body
response = requests.put(url,request_json_body,auth=('PO','PO@pp123'),headers={'content-type':'application/json'})
Status = response.status_code
RespStatus = str(Status)

if Status == 200 :
    print ("Authorization Successfull")
else :
    Error = StatusCodes.stagger(Status)
    Auth_Error = str(Error)
    print ("Authorization Fault :"+" "+RespStatus+" : "+Auth_Error)


