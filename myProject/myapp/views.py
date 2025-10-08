from django.shortcuts import render #conversion of raw file to web page

# Create your views here.
def index(request):
    return render(request, 'index.html')

