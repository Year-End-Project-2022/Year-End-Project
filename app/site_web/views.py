from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'site_web/index.html')
