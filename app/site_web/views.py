from django.shortcuts import render


def index(request):
    return render(request, 'site_web/index.html')


def news(request):
    return render(request, 'site_web/news.html')


def ateliers(request):
    return render(request, 'site_web/ateliers.html')


def about(request):
    return render(request, 'site_web/about.html')
