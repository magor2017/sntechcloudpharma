from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
import pymysql.cursors
import json


# Create your views here.
def index(request):
    return render(request,'login/index.html')
def connexion(request):
    return render(request,'login/connexion.html')

@method_decorator(csrf_exempt)
def auth(request):
    iD='cloudpharma'
    password='cloudpharma'
    req=json.loads(request.body)
    if iD==req['id'] and password==req['password']:
        return JsonResponse({'erro':'identifier'})
    else:
        return JsonResponse({'erro':'echec'})

