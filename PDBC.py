#pdbc programming
import cx_Oracle
con=cx_Oracle.connect('system/teju12345@localhost')
if con!=None:
    print("Connected Successufully")
    print("Version: ",con.version)
else:
    print("Connection Failed")
con.close()
