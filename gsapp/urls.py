from django.urls import path
from gsapp import views

urlpatterns = [
    path('',views.Regiser_user,name='registration' ),
    path('sstd/',views.save_std_details,name='sstd')
]