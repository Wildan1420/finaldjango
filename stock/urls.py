from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('About', views.About, name='About'),
    path('Contact', views.Contact, name='contact'),

]
