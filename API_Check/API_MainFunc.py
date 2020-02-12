import AckPO
import Update_DueDate
import DisputePO


def main() :
    print ("------ Acknowledgement ------")
    Ack_PO = AckPO.AcknwldgPO()
    print (Ack_PO)
    print ("------ Due Date Update ------")
    DueDate_Updt = Update_DueDate.dueDateUpdate()
    print (DueDate_Updt)
    print ("------ Dispute PO ------")
    Dispute_PO = DisputePO.disputePO()
    print (Dispute_PO)


if __name__ == "__main__":
    main()

