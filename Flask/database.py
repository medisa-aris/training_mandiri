# importing required library 
import mysql.connector
  
def querydata(sql="select 'none'"):
    # connecting to the database 
    dataBase = mysql.connector.connect(
                        host = <your_host>,
                        user = <your_username>,
                        passwd = <your_password>,
                        database = <your_database_name> ) 
    
    # preparing a cursor object 
    cursorObject = dataBase.cursor(dictionary=True) 

    # selecting query
    cursorObject.execute(sql)
    
    myresult = cursorObject.fetchall()
    
    # for x in myresult:
    #     print(x)
    
    # disconnecting from server
    dataBase.close() 

    return myresult

result = querydata()
print(result)
