from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
import pymysql.cursors


# Create your views here.
def index(request):
    return render(request,'login/index.html')
def connexion(request):
    return render(request,'login/connexion.html')

@csrf_exempt
def verifData(request):
    id='cloudpharma'
    password='cloudpharma'
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='cloudpharma',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    t=""
    with connection.cursor() as cursor:
        sql="SELECT * FROM users WHERE identifiant=%s AND password=%s"
        cursor.execute(sql,(id,password,))
        t=cursor.fetchone()
    
    if id==request.POST['id'] and password==request.POST['password']:
        return JsonResponse({'erro':t})
    else:
        return JsonResponse({'erro':t})

