import requests
import json
import StatusCodes
import Database_Query
import PropertyFile
import datetime
import ExcelFunc

def dueDateUpdate() :
    # API URI
    url = PropertyFile.getValue('URI','po_update_duedate')

    # Read input json file
    file = open(PropertyFile.getValue('JSON_PATH','po_duedate_json'),'r')
    json_input = file.read()

    # Convert the string from the input file into Json format
    request_json = json.loads(json_input)
    request_json_body = json.dumps(request_json)

    # Make Post Request with Json Input body
    response = requests.put(url,request_json_body,auth=('PO','PO@pp123'),headers={'content-type':'application/json'})
    Status = response.status_code
    #print (Status)
    ExcelFunc.WriteIntoExcel(1,3,Status)

    # Extract the comparison values : Due Date from the request Json
    # create a List and append all the Json Array values into the List ( P.S Easy to retrieve values one after the other )
    yearlist = []
    Json_Type = request_json.get('PoLineItems')

    for d in Json_Type:
        for key, value in d.iteritems():
            yearlist.append(value)

    Line_1_DueDate = yearlist[0]

    # Extract the comparision values : Due Date from DataBase
    DB_DueDate = Database_Query.DB_Connect("SELECT DueDate FROM [PSMIApps].[dbo].[tbl_IssuePurchaseOrderHeader] where PONum = 9998180")
    DB_Line_1_DueDate = Database_Query.DB_Connect("SELECT LineDueDate FROM [PSMIApps].[dbo].[tbl_IssuePurchaseOrderLine] where PONum = 9998180 and LineNum = 1")
    DB_Line_2_DueDate = Database_Query.DB_Connect("SELECT LineDueDate FROM [PSMIApps].[dbo].[tbl_IssuePurchaseOrderLine] where PONum = 9998180 and LineNum = 2")

    # convert the DB date format to the comparable date value
    ConCat_Str_Val_Header = PropertyFile.getDateFormat(DB_DueDate)
    ConCat_Str_Val_One = PropertyFile.getDateFormat(DB_Line_1_DueDate)

    # Verify if the Response Code is Success
    if (Status >=200 and Status < 300):
            print ("Status is"+" "+str(Status))
    else:
            #print ("Status is"+" "+str(Status))
            ExcelFunc.WriteIntoExcel(1, 4, 'Fail')
            exit()

    #print (Line_1_DueDate)
    #print (ConCat_Str_Val_Header)

    # compare DueDate header to see if it is same as the Line Level value
    if ( Line_1_DueDate == ConCat_Str_Val_Header):
        #print ("Database Due Date updated in the PO Header level")
        return ("Pass - Status is" + " " + str(Status))
    else:
        #print ("Database Due Date not updated in the PO Header level")
        ExcelFunc.WriteIntoExcel(1, 4, 'Fail')
        return ("Fail - Status is" + " " + str(Status))
        exit()

    #print (Line_1_DueDate)
    #print (ConCat_Str_Val_One)

    # compare Line 1 DueDate with the Line 2 Due Date
    if ( Line_1_DueDate == ConCat_Str_Val_One):
        #print ("Database Due Date is updated for Line 1")
        ExcelFunc.WriteIntoExcel(1, 4, 'Pass')
        exit()
    else:
        #print ("Database Due Date is not updated for Line 1")
        ExcelFunc.WriteIntoExcel(1, 4, 'Fail')
        exit()