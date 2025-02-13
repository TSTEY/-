from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('service_details/',views.service_details,name='service_details'),
    path('starter_page/',views.starter_page,name='starter_page'),
    path('admin/',views.admin,name='admin'),
    
    path('header/',views.header,name='header'),
    path('block_one/',views.block_one,name='block_one'),
    path('block_two/',views.block_two,name='block_two'),
    path('block_three/',views.block_three,name='block_three'),
    path('block_four/',views.block_four,name='block_four'),
    path('block_five/',views.block_five,name='block_five'),
    path('block_six/',views.block_six,name='block_six'),
    path('block_seven/',views.block_seven,name='block_seven'),
    path('block_eight/',views.block_eight,name='block_eight'),
    path('block_nine/',views.block_nine,name='block_nine'),
    path('block_ten/',views.block_ten,name='block_ten'),
    path('footer/',views.footer,name='footer'),
    
]