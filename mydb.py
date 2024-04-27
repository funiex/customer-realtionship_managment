import   mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd ='vijay@8009907770'
    
    )
#prepare a cursor object

cursorObject = dataBase.cursor()

cursorObject.execute( "CREATE DATABASE elderco")

print( "all done ")