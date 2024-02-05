#importing for sql connection
import mysql.connector as cnt
from datetime import datetime
#imprting for email services
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from concurrent.futures import ThreadPoolExecutor
import getpass
###################################################


class Dbs:
    def __init__(self):
        self.connection=cnt.connect(host="localhost",
                                    user="root",
                                    password="Root@root")
    def ShowDatabases(self):
        qry="show databases"
        cursor=self.connection.cursor()
        cursor.execute(qry)
        databases=cursor.fetchall()
        for database in databases:
            print(database[0])
            
    def useDatabase(self,DatabaseName):
        cursor=self.connection.cursor()
        qry="use {}".format(DatabaseName)
        cursor.execute(qry)
        print("database changed {}".format(DatabaseName))
    
    def createDatabase(self,DBName):
        cursor=self.connection.cursor()
        qry = "CREATE DATABASE IF NOT EXISTS {}".format(DBName)
        cursor.execute(qry)
        print("database created with {} name".format(DBName))
        print("list of databases")
        self.ShowDatabases()

    def showTables(self):
        cursor=self.connection.cursor()
        qry="show tables"
        cursor.execute(qry)
        tables=cursor.fetchall()
        for table in tables:
            print(table[0])
    def createTable (self,TableName):
        qry= """CREATE TABLE IF NOT EXISTS {} (userid INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255)NOT NULL,
        email_id VARCHAR(255) NOT NULL,
        uid VARCHAR(255) NOT NULL)""".format(TableName)
        cursor=self.connection.cursor()
        cursor.execute(qry)
        self.connection.commit()
        print("{} table created".format(TableName))
    
    def InsertValues(self,table_name,F_name,L_name,Email,Uid):
        qry= """
        insert into {} (first_name,last_name,email_id,uid)
        values (%s,%s,%s,MD5(%s))
        """.format(table_name)
        values=(F_name,L_name,Email,Uid)
        cursor=self.connection.cursor()
        cursor.execute(qry,values)
        self.connection.commit()
        print("value inserted")
    def viewTableData(self,tableName):
        cursor=self.connection.cursor()
        qry="select * from {}".format(tableName)
        cursor.execute(qry)
        TableData=cursor.fetchall()
        for data in TableData:
            print(data[0::])
    def DelTable (self,TableName):
        qry="drop table {}".format(TableName)
        cursor=self.connection.cursor()
        cursor.execute(qry)
        #self.connection.commitm()
        print("{} deleted".format(TableName))
        
        
    def selectionTable(self,NewTableName,SelectingFrom,limitNumber):
        #qry = " select email_id from {} limit {}".format(tableName,limitNumber)
        qry="""create table if not exists {} as 
        select email_id , uid from {} limit {}""".format(NewTableName,SelectingFrom,limitNumber)
        cursor=self.connection.cursor()
        cursor.execute(qry)
        self.connection.commit()
        print("new table created with name {}".format(NewTableName))
        qry= """
        select * from {}
        """.format(NewTableName)
        cursor.execute(qry)
        data2=cursor.fetchall()
        for data in data2:
            print(data)  

    def sendingList(self,TableName):
        qry="select * from {}".format(TableName)
        cursor=self.connection.cursor()
        cursor.execute(qry)
        data=cursor.fetchall()
        EmailList=[]
        uid=[]
        for gettin in data:
            EmailList.append(gettin[0])
            uid.append(gettin[1])
            print(gettin)
        return EmailList
    

        


    def CloseCunnection(self):
        self.connection.close()
        print("connection closed")
###########################################
        




#main codes        
#db=Dbs()

#db.ShowDatabases()
#db.createDatabase("day2")
#db.useDatabase("day2")
#db.createTable("day2Table")
#db.InsertValues("day2Table","Roshan","Kumar","roshan@email.com","001")
"""db.InsertValues("day2Table",'Praful', 'Gupta', 'praful@gmail.com',"002")
db.InsertValues("day2Table",'Vivek', 'pandey', 'vivek.pandey@outlook.com',"003")
db.InsertValues("day2Table",'Harsh', 'Kumar', 'harsh.kumar@info.com',"004")
db.InsertValues("day2Table",'Ashish', 'Baisoya', 'ashishbaisoya@alpha.com',"005")
db.InsertValues("day2Table",'Roshan', 'Kumar', 'roshan.kumar@bita.com',"006")
"""
#db.showTables()
#db.viewTableData("day2Table")
#db.selectionTable("Selection","day2Table",5)
#db.viewTableData("selection")
#db.sendingList("Selection")

#db.CloseCunnection()
