import ConfigParser

config = ConfigParser.ConfigParser()

# Function to set the Attributes of Json Values
def getValue(Attrb1, Attrb2):
    config.read('config.ini')
    Value = config.get(Attrb1, Attrb2)
    return Value

# Function to set the Format of Date Values
def  getDateFormat(DBDate):
    Month = DBDate.strftime('%m')
    Date = (DBDate.strftime('%d'))
    Year = str(DBDate.year)
    DateVal = Month + '/' + Date + '/' + Year
    return DateVal
