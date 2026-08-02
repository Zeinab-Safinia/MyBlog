
from django.urls import path
from website.views import *

urlpatterns = [
    #path ('url address' , 'view')
    path('', index_view),
    #we can dont write home here
    path('about', about_view),
    path('contact', contact_view)
    
]