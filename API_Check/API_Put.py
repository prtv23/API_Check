import responses
import requests
import json
import StatusCodes
import jsonpath
import grequests

# API URI
url = "http://192.168.2.7:6080/api/purchaseorders/AcknowledgePO"

# Read input json file
file = open('C:\Users\CE341\Desktop\Python\API_TestData.txt','r')
json_input = file.read()

# Convert the string from the input file into Json format
request_json = json.loads(json_input)

# Make Post Request with Json Input body
response = requests.put(url,request_json)

# parse into json
response_json = json.loads(response.text)
Status = (response_json.get('Data')).get('Status')
StatusCodes.stagger(Status)
