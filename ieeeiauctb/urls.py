
from django.urls import path

from ieeeiauctb.views import contactus, register
from . import views


urlpatterns = [
    path('',views.homepage, name='index'),
    path('registerform',views.register,name='register'),
    path('tamasbama',views.contactus,name='contact'),
    path('login',views.login,name='login')
]