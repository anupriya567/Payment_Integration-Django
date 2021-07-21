from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('success/' ,views.success , name='success'),
    path('course/' ,views.course, name='course'),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('donate/',views.donate,name="donate"),
     
]