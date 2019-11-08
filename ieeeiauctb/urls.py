
from django.urls import path

from . import views


urlpatterns = [
    path('',views.index),
    path('index.html',views.homepage),
    path('registerform.html',views.register),
    path('tamasbama.html',views.contactus),
    path('registerform.html',views.signup),
]