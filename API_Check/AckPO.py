import requests
import json
import Database_Query
import PropertyFile
import ExcelFunc

def AcknwldgPO() :

    # API URI
    url = PropertyFile.getValue('URI','po_acknowledge')

    # Read input json file
    file = open(PropertyFile.getValue('JSON_PATH','po_acknowledge_json'),'r')
    json_input = file.read()

    # Convert the string from the input file into Json format
    request_json = json.loads(json_input)
    request_json_body = json.dumps(request_json)

    # Make Post Request with Json Input body
    response = requests.put(url,request_json_body,auth=('PO','PO@pp123'),headers={'content-type':'application/json'})
    Status = response.status_code
    #print (Status)
    ExcelFunc.WriteIntoExcel(2, 3, Status)

    # Extract the comparison values : AckDate, Expected Shipment Date in the Header and Line from the json input file
    # Extract Acknowledgement Date
    Json_AckDate = request_json.get('AckDate')
    Json_Header_AckDate_Val = str(Json_AckDate)

    # Extract Expected Shipment Dates for both Line 1 and Line 2
    yearlist = []
    Json_Type = request_json.get('AcknowledgedPoLines')

    for d in Json_Type:
        for key, value in d.iteritems():
            yearlist.append(value)

    ExpShipDate_Line_1 = yearlist[0]

    # Extract values from the Database
    DB_Header_Val = Database_Query.DB_Connect("select PoAcknowledgementDate from [PSMIApps].[dbo].[tbl_IssuePurchaseOrderHeader] where PONum = 9998174")
    DB_Line_1_Val = Database_Query.DB_Connect("select ExpectedShipDate from [PSMIApps].[dbo].[tbl_IssuePurchaseOrderLine] where PONum = 9998174 and LineNum = 1")

    # Format Date values to suite the comparison
    Formatted_Header_DB_Date = PropertyFile.getDateFormat(DB_Header_Val)
    Formatted_Line_1_Date = PropertyFile.getDateFormat(DB_Line_1_Val)
    #Formatted_Line_2_Date = PropertyFile.getDateFormat(DB_Line_2_Val)

    # Verify if the Response Code is Success
    # Verify if the Response Code is Success
    if (Status >=200 and Status < 300):
            print ("Status is"+" "+str(Status))
    else:
            print ("Status is"+" "+str(Status))
            ExcelFunc.WriteIntoExcel(2, 4, 'Fail')
            return ("Fail - Status is"+" "+str(Status))
            exit()

    # Compare Json Input Header Value with DB Header Value
    if (Json_Header_AckDate_Val == Formatted_Header_DB_Date):
        print ("Acknowledgement Date successfully updated at the header level")
    else:
        print ("Acknowledgement Date is not updated at the header level")
        ExcelFunc.WriteIntoExcel(2, 4, 'Fail')
        exit()

    # Compare Json Input Line 1 with the DB Line 1 Expected Shipment Date
    if (ExpShipDate_Line_1 == Formatted_Line_1_Date):
        #print ("Expected Shipment Date for the Line 1 is updated")
        ExcelFunc.WriteIntoExcel(2, 4, 'Pass')
        return ("Pass - Status is" + " " + str(Status))
        exit()
    else:
        print ("Expected Shipment Date for the Line 1 is not updated")
        ExcelFunc.WriteIntoExcel(2, 4, 'Fail')
        exit()