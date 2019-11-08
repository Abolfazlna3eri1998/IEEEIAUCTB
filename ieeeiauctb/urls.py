
from django.urls import path

from ieeeiauctb.views import contactus, register
from . import views


urlpatterns = [
    path('',views.index, name='base'),
    path('index.html',views.homepage, name='index'),
    path('registerform.html',views.register,name=register),
    path('tamasbama.html',views.contactus,name=contactus),
    path('login.html',views.login,name=login)
]