from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index_view(request):
    return render(request, 'web/index.html')
def about_view(request):
    return render(request, 'web/about.html')
def contact_view(request):
    return render(request, 'web/contact.html')