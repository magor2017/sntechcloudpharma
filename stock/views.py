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

