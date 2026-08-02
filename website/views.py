from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index_view(request):
    return HttpResponse('<h1>This is home page</h1>')
def about_view(request):
    return HttpResponse('<h1>This is about page</h1>')
def contact_view(request):
    return HttpResponse('<h1>This is contact page</h1>')