from django.urls import path
from . import views
app_name='vendeur'




urlpatterns=[
    path('accueil/',views.accueil,name='accueil'),
]