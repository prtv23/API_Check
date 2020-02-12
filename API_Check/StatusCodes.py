def stagger(arguement):
    MK = {
       200 : "Success",
       201 : "New Entry Created",
       204 : "No Content",
       400 : "Bad Request",
       404 : "Record Not Found For Input Specifiec",
       401 : "Unauthorized",
       500 : "Internal Server Error"
    }
    return MK.get(arguement)




