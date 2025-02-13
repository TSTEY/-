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
    
    # Header
    path('create_header/',views.create_header,name='create_header'),
    path('update_header/<int:user_id>/',views.update_header,name='update_header'),
    path('delete_header/<int:user_id>/',views.delete_header,name='delete_header'),
    
    # Block
    
    # One
    path('create_block_one/',views.create_block_one,name='create_block_one'),
    path('update_block_one/<int:user_id>/',views.update_block_one,name='update_block_one'),
    path('delete_block_one/<int:user_id>/',views.delete_block_one,name='delete_block_one'),
    
    # Two
    path('create_block_two/',views.create_block_two,name='create_block_two'),
    path('update_block_two/<int:user_id>/',views.update_block_two,name='update_block_two'),
    path('delete_block_two/<int:user_id>/',views.delete_block_two,name='delete_block_two'),
    
    # Three
    path('create_block_three/',views.create_block_three,name='create_block_three'),
    path('update_block_three/<int:user_id>/',views.update_block_three,name='update_block_three'),
    path('delete_block_three/<int:user_id>/',views.delete_block_three,name='delete_block_three'),
    
    # Four
    path('create_block_four/',views.create_block_four,name='create_block_four'),
    path('update_block_four/<int:user_id>/',views.update_block_four,name='update_block_four'),
    path('delete_block_four/<int:user_id>/',views.delete_block_four,name='delete_block_four'),
    
    # Five
    path('create_block_five/',views.create_block_five,name='create_block_five'),
    path('update_block_five/<int:user_id>/',views.update_block_five,name='update_block_five'),
    path('delete_block_five/<int:user_id>/',views.delete_block_five,name='delete_block_five'),
    
    # Six
    path('create_block_six/',views.create_block_six,name='create_block_six'),
    path('update_block_six/<int:user_id>/',views.update_block_six,name='update_block_six'),
    path('delete_block_six/<int:user_id>/',views.delete_block_six,name='delete_block_six'),
    
    # Seven
    path('create_block_seven/',views.create_block_seven,name='create_block_seven'),
    path('update_block_seven/<int:user_id>/',views.update_block_seven,name='update_block_seven'),
    path('delete_block_seven/<int:user_id>/',views.delete_block_seven,name='delete_block_seven'),
    
    # Eight
    path('create_block_eight/',views.create_block_eight,name='create_block_eight'),
    path('update_block_eight/<int:user_id>/',views.update_block_eight,name='update_block_eight'),
    path('delete_block_eight/<int:user_id>/',views.delete_block_eight,name='delete_block_eight'),
    
    # Nine
    path('create_block_nine/',views.create_block_nine,name='create_block_nine'),
    path('update_block_nine/<int:user_id>/',views.update_block_nine,name='update_block_nine'),
    path('delete_block_nine/<int:user_id>/',views.delete_block_nine,name='delete_block_nine'),
    
    # Ten
    path('create_block_ten/',views.create_block_ten,name='create_block_ten'),
    path('update_block_ten/<int:user_id>/',views.update_block_ten,name='update_block_ten'),
    path('delete_block_ten/<int:user_id>/',views.delete_block_ten,name='delete_block_ten'),
    
    
    # Footer
    path('create_footer/',views.create_footer,name='create_footer'),
    path('update_footer/<int:user_id>/',views.update_footer,name='update_footer'),
    path('delete_footer/<int:user_id>/',views.delete_footer,name='delete_footer'),
    
]