from django.urls import path
from . import views
app_name='vendeur'




urlpatterns=[
    path('accueil/',views.accueil,name='accueil'),
    path('vente/',views.vente,name='vente'),
    path('getProducts/',views.getProducts,name='getProducts'),
    path('saveBill/',views.saveBill),
    path('getProductsByDate/',views.getProductsByDate),
    path('getProductsByInterval',views.getProductsByInterval),
]