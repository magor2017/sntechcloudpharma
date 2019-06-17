from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from datetime import date
import pymysql.cursors
from . import model
from random import randint

# Create your views here.
def accueil(request):
    return render(request,'vendeur/accueil.html')

def vente(request):
    #return render(request,'vendeur/vente.html')
    return JsonResponse({"data":"data"})

@method_decorator(csrf_exempt)
def getProducts(request):
    """"
    products=[
            {"id":1,"name":"product1","prix":2000},
            {"id":2,"name":"adama1","prix":4000},
            {"id":3,"name":"goudiaby2","prix":3000},
            {"id":3,"name":"rasta","prix":3000}
        ]
    """
    con=model.connect()
    pr=str(json.loads(request.body)['prod'])
    products=model.getProductsByName(con,pr)
    prods=[]
    for l in products:
        if l["ProductTitle"].startswith(str(json.loads(request.body)['prod'])):
            prods.append(l)
    #print(dir(request.POST.copy))
    return JsonResponse({"data":prods,"post":str(json.loads(request.body)['prod'])})
@method_decorator(csrf_exempt)
def saveBill(request):
    data=json.loads(request.body)
    billId=int(str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9)))
    bill=(
        billId,
        datetime.now(),
        data['products'],
        data['idUser'],
        data['total'],
        2
    )
    con=model.connect()
    model.saveBill(bill,con)
    products=json.loads(data['products'])
    for p in products:
        model.saveSelling((billId,p['quantite'],p['ProductId'],p['SellingPriceOfUnit']),con)
    r=con.commit()
    model.disconnect(con)
    return JsonResponse({"data":"1","res":r})
@method_decorator(csrf_exempt)
def getProductsByDate(request):
    data=json.loads(request.body)
    Date=date.today() if data['date']=="" else data['date']
    con=model.connect()
    result=model.getProductsByDate(con,Date)
    model.disconnect(con)
    return JsonResponse({"data":result})
@method_decorator(csrf_exempt)
def getProductsByInterval(request):
    data=json.loads(request.body)
    date1=data['date1'].split('-')
    date2=data['date2'].split('-')
    datetime1=datetime(int(date1[0]),int(date1[1]),int(date1[2]))
    datetime2=datetime(int(date2[0]),int(date2[1]),int(date2[2]))
    print(datetime1)
    con=model.connect()
    result=model.getProductsByInterval(con,datetime1,datetime2)
    model.disconnect(con)
    return JsonResponse({"data":result})


