from django.urls import path, re_path
from . import views

app_name='polls'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('home/', views.home),
    # path('showform/', views.showform, name='showform'),
    # path('getform/', views.getform, name='getform'),
    # path('dishes/<str:dish>', views.menuitems),
    # path('menu_item/10', views.display_menu_item),
    # re_path(r'^menu_item/([0-9]{2})/$', views.display_menu_item),
    # path('index/', views.index, name='index'),
    # path('login/', views.login, name='login'),
    path('home/', views.form_view, name='form'),
    path('booking/', views.booking_view, name="booking")
    
]

 #  reverse('polls:index')