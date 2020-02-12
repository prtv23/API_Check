import xlrd
import xlwt
from xlutils.copy import copy

# open excel file
book = xlrd.open_workbook("API_TestCases_PSMI.xls")
# point to the sheet to be opened
Sheet = book.sheet_by_index(0)

# URI for update po due date
Excel_Val = (Sheet.cell(1, 2))
URI_DueDt = str(Excel_Val)
URI_UpdDueDt = URI_DueDt[7:72]

# URI for Acknowledge PO
Excel_Val = Sheet.cell(2,2)
URI_Ack = str(Excel_Val)
URI_AckPo = URI_Ack[7:70]

# # URI for Dispute PO
# Excel_Val = Sheet.cell(3,2)
# URI_Dispute = str(Excel_Val)
# URI_DispPo = URI_Dispute[7:66]

def WriteIntoExcel(Row,Col, Status):
    rb = xlrd.open_workbook('API_TestCases_PSMI.xls')
    wb = copy(rb)
    w_sheet = wb.get_sheet(0)
    w_sheet.write(Row,Col,Status)
    #w_sheet.write(1, 4, 'Pass')
    wb.save('API_TestCases_PSMI.xls')










