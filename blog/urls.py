
from django.urls import path
from blog.views import *


app_name = 'blog'

urlpatterns = [
    #path ('url address' , 'view')
    path('', blog_view, name='index'),
    path('single', blog_single, name='single'),
    path('single/post-<int:pid>', post_view, name='post_view'),
]