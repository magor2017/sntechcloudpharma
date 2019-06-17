from django.urls import path
from . import views
app_name='stock'




urlpatterns=[
    path('addProduct/',views.addProduct),
    path('listProduct/',views.listProduct),
    path('listProductByRayon/',views.listProductByRayon),
    path('deleteProduct/',views.deleteProduct),
]
    