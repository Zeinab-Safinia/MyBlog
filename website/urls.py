
from django.urls import path
from website.views import *


app_name = 'website'

urlpatterns = [
    #path ('url address' , 'view')
    path('', index_view, name='index'),
    #we can dont write home here
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    
]