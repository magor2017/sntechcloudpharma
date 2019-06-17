import pymysql.cursors
from datetime import datetime

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
def addProduct(con,data):
    cursor=con.cursor()
    date=datetime.now()
    peremp=""
    if data['peremption']!="":
        peremp=data['peremption']
    else:
        peremp=None
    if getProductByName(con,data['nom'].lower())==None:
        try:
            sql="INSERT INTO `products` (`ProductTitle`,`ProductDescription`,`NumberUnitsProduct`,`UnitsInStock`,`ReoderLevel`,`Tva`,`SellingPriceOfUnit`,`PurchasePriceOfUnit`,`CategorieId`,`peremption`,`rayon`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            row=cursor.execute(sql,(data['nom'].lower(),data['description'].lower(),data['quantite'],data['quantite'],0,data['tva'],data['sellingPrice'],data['purchasePrice'],0,peremp,int(data['rayon'])))
            con.commit()
            return row
        except:
            return 0
    else:
        return -1

def listProduct(con):
    cursor=con.cursor()
    #awa faye
    sql="SELECT * FROM products WHERE etat=1"
    cursor.execute(sql)
    return cursor.fetchall()

def getProductByName(con,name):
    cursor=con.cursor()
    sql="SELECT * FROM `products` WHERE `ProductTitle`=%s AND etat=1"
    cursor.execute(sql,(name))
    p=cursor.fetchone()
    return p

def listProductByRayon(con,rayon):
    cursor=con.cursor()
    sql="SELECT * FROM `products` WHERE `rayon`=%s AND etat=1"
    cursor.execute(sql,(rayon))
    p=cursor.fetchall()
    return p

def deleteProduct(con,id):
    cursor=con.cursor()
    sql1="SELECT * FROM selling WHERE ProductId=%s"
    cursor.execute(sql1,(id))
    p=cursor.fetchone()
    if p==None:
        sql="UPDATE `products` SET `etat`=0 WHERE `ProductId`=%s"
        r=cursor.execute(sql,(id))
        con.commit()
        return r
    else:
        return -1