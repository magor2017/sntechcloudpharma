import pymysql.cursors
from random import randint


def connect():
    con=''
    try:
        con=pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='BD_CLOUDSTOCKMANAGER',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
    except:
        con=''
    return con
def disconnect(con):
    con.close()
def saveBill(data,con):
    #con=connect()
    if con.open:
        cursor=con.cursor()
        sql = "INSERT INTO `Bills` (`BILLNumber`,`BILLDate`,`InfoSup`,`EmployeId`,`TotalPrice`,`SellingType`) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, data)
        #con.commit()
def saveSelling(data,con):
    if con.open:
        cursor=con.cursor()
        sql="INSERT INTO `Selling` (`BILLNumber`, `NumberOfUnits`,`ProductId`,`SellingPrice`) VALUES (%s, %s,%s,%s)"
        cursor.execute(sql,data)
def getProductsByDate(con,date):
    if con.open:
        cursor=con.cursor()
        sql="SELECT * FROM `Bills` WHERE BILLDate LIKE "+"'%"+str(date)+"%'"
        cursor.execute(sql)
        data=cursor.fetchall()
        return data
    else:
        return []
def getProductsByInterval(con,date1,date2):
    if con.open:
        cursor=con.cursor()
        #sql="SELECT * FROM `Bills` WHERE BILLDate >= '"+str(date1)+"' AND BILLDate <='"+str(date2)+"'"
        sql="SELECT * FROM `Bills` WHERE BILLDate >= %s AND BILLDate <=%s"
        cursor.execute(sql,(str(date1),str(date2)))
        data=cursor.fetchall()
        return data
    else:
        return []
def getProductsByName(con,p):
        if con.open:
                cursor=con.cursor()
                sql="SELECT * FROM `products` WHERE `ProductTitle` LIKE "+"'%"+str(p)+"%'"
                cursor.execute(sql)
                data=cursor.fetchall()
                return data
        else:
                return []

