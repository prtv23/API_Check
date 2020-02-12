import ConfigParser
import ExcelFunc


if __name__ == "__main__":
    config = ConfigParser.ConfigParser()

    # add All Sections into the Config Parser
    config.add_section('DataBase')
    config.add_section('URI')
    config.add_section('JSON_PATH')
    config.add_section('API_Config')

    # set All DB values in the Config Parser
    config.set('DataBase', 'PSMI', 'DRIVER={SQL SERVER};server=10.1.1.190;database=PSMIApps;uid=EGCConnection;pwd=EG6#2019')
    config.set('DataBase', 'VP', 'DRIVER={SQL SERVER};server=192.168.2.7;database=PSMI_VENDOR_QA;uid=psmi_dev;pwd=Psm!us3r')

    # set All API URI's in the Config Parser
    config.set('URI', 'po_dispute', ExcelFunc.URI_DispPo)
    config.set('URI', 'po_update_duedate', ExcelFunc.URI_UpdDueDt)
    config.set('URI', 'po_acknowledge', ExcelFunc.URI_AckPo)

    # set All Json Path's into the Config Parser
    config.set('JSON_PATH','PO_Dispute_JSON','C:\Users\CE341\Desktop\Python\PO_Dispute_Json.txt')
    config.set('JSON_PATH','PO_DueDate_JSON','C:\Users\CE341\Desktop\Python\PO_DueDate_Json.txt')
    config.set('JSON_PATH', 'PO_Acknowledge_JSON', 'C:\Users\CE341\Desktop\Python\Acknowledgement_Json.txt')

    # json constants
    config.set('API_Config','Auth',('PO','PO@pp123'))

    with open('config.ini', 'w') as configfile:
        config.write(configfile)


