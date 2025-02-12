from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('service_details/',views.service_details,name='service_details'),
    path('starter_page/',views.starter_page,name='starter_page'),
]