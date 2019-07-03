from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from . import model

# Create your views here.
@method_decorator(csrf_exempt)
def addProduct(request):
    data=json.loads(request.body)
    con=model.connect()
    row=model.addProduct(con,data)
    model.disconnect(con)
    return JsonResponse({"row":row})

@method_decorator(csrf_exempt)
def listProduct(request):
    con=model.connect()
    result=model.listProduct(con)
    model.disconnect(con)
    return JsonResponse({"data":result})

@method_decorator(csrf_exempt)
def listProductByRayon(request):
    data=json.loads(request.body)
    con=model.connect()
    result=model.listProductByRayon(con,int(data['rayon']))
    model.disconnect(con)
    return JsonResponse({"data":result})

@method_decorator(csrf_exempt)
def deleteProduct(request):
    data=json.loads(request.body)
    con=model.connect()
    result=model.deleteProduct(con,data['id'])
    model.disconnect(con)
    return JsonResponse({"data":result})

@method_decorator(csrf_exempt)
def updateProduct(request):
    data=json.loads(request.body)
    attribut=data['attribut']
    param=data['param']
    ProductId=int(data['ProductId'])
    con=model.connect()
    reponse={}
    for p in attribut:
        if p=="ProductTitle":
            par=(param[p],ProductId)
            tontou=model.updateProductTitle(con,par)
            reponse['ProductTitle']=tontou
        if p=="ProductDescription":
            par=(param[p],ProductId)
            tontou=model.updateProductDescription(con,par)
            reponse["ProductDescription"]=tontou
        if p=="UnitsInStock":
            par=(param[p],ProductId)
            tontou=model.updateUnitsInStock(con,par)
            reponse["UnitsInStock"]=tontou
        if p=="SellingPrice":
            par=(param[p],ProductId)
            tontou=model.updateSellingPrice(con,par)
            reponse["SellingPrice"]=tontou
        if p=="PurchasePriceOfUnit":
            par=(param[p],ProductId)
            tontou=model.updatePurchasePrice(con,par)
            reponse["PurchasePriceOfUnit"]=tontou
        if p=="Peremption":
            par=(param[p],ProductId)
            tontou=model.updatePeremption(con,par)
            reponse["Peremption"]=tontou
        if p=="tva":
            par=(int(param["Tva"]),ProductId)
            tontou=model.updateTva(con,par)
            reponse["tva"]=tontou
    #con=model.connect()
    #result=model.updateProductTitle()
    return JsonResponse({"data":reponse})

