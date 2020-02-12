import requests
import json
import StatusCodes
import Database_Query
import PropertyFile
from xlwt import Workbook
import ExcelFunc

def disputePO():
    # API URI
    url = PropertyFile.getValue('URI','po_dispute')

    # Read input json file
    file = open(PropertyFile.getValue('JSON_PATH','po_dispute_json'),'r')
    json_input = file.read()

    # Convert the string from the input file into Json format
    request_json = json.loads(json_input)
    request_json_body = json.dumps(request_json)

    # Make Post Request with Json Input body
    response = requests.put(url,request_json_body,auth=('PO','PO@pp123'),headers={'content-type':'application/json'})
    Status = response.status_code
    #print (Status)
    ExcelFunc.WriteIntoExcel(3,3,Status)

    # Extract the comparison values : Dispute Date, Dispute Type, Dispute Revision & Comment from the json input file
    Json_Date = request_json.get('DisputeDate')
    Str_Json_Date = str(Json_Date)

    # create a List and append all the Json Array values into the List ( P.S Easy to retrieve values one after the other )
    yearlist = []
    Json_Type = request_json.get('DisputeItems')

    for d in Json_Type:
        for key, value in d.iteritems():
            yearlist.append(value)

    Str_Json_Type = yearlist[2]
    Str_Json_Revision = yearlist[0]
    Str_Json_Comment = yearlist[1]

    # Validate if the Due Date in the DB is updated to the Input Due Date
    DB_DisputeDate = Database_Query.DB_Connect("SELECT AckHoldDate FROM [PSMIApps].[dbo].[tbl_IssuePurchaseOrderHeader] where PONum = 9998183")
    DB_DisputeType = Database_Query.DB_Connect("SELECT AckHoldType FROM [PSMIApps].[dbo].[tbl_IssuePurchaseOrderHeader] where PONum = 9998183")
    DB_DisputeComment = Database_Query.DB_Connect("SELECT AckHoldComments FROM [PSMIApps].[dbo].[tbl_IssuePurchaseOrderHeader] where PONum = 9998183")

    # Format Date values to suite the comparison
    DB_New_DisputeDate = PropertyFile.getDateFormat(DB_DisputeDate)

    # Verify if the Response Code is Success
    if (Status >=200 and Status < 300):
            print ("Status is"+" "+str(Status))
            return ("Pass - Status is" + " " + str(Status))
    else:
            print ("Status is"+" "+str(Status))
            ExcelFunc.WriteIntoExcel(3, 4, 'Fail')
            return ("Fail - Status is" + " " + str(Status))
            exit()

    # Compare Dispute Date in Json Input File to the Database Value
    if (Str_Json_Date == DB_New_DisputeDate):
        print ("Dispute Date Update Successful for the PO record")
    else:
        print ("Dispute Date not updated")
        ExcelFunc.WriteIntoExcel(3, 4, 'Fail')
        exit()

    # Compare Dispute Type in Json Inout File to Database Value
    if (Str_Json_Type == DB_DisputeType ):
        print ("Dispute Type has been successfully updated")
    else:
        print ("Dispute Type is not updated")
        ExcelFunc.WriteIntoExcel(3, 4, 'Fail')
        exit()

    # Compare Dispute Comments in Json Inout File to Database Value
    if (Str_Json_Comment == DB_DisputeComment):
        print ("Dispute Comment has been successfully updated")
        ExcelFunc.WriteIntoExcel(3, 4, 'Pass')
        exit()
    else:
        print ("Dispute Comments are not updated")
        ExcelFunc.WriteIntoExcel(3, 4, 'Fail')
        exit()