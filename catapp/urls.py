from django.urls import path
from catapp import views

urlpatterns = [

    path('',views.home,name="home"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('cat',views.cat,name="cat"),
    path('contact', views.contact, name='contact'),
]
