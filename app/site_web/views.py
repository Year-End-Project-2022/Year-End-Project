from django.shortcuts import render
from .models import ImageGalerie


def index(request):
    return render(request, 'site_web/index.html')


def news(request):
    return render(request, 'site_web/news.html')


def ateliers(request):
    return render(request, 'site_web/atelier/ateliers.html')


def calendrier(request):
    return render(request, 'site_web/atelier/calendrier.html')


def machines(request):
    return render(request, 'site_web/machines.html')


def tarifs(request):
    return render(request, 'site_web/tarifs.html')


def adhesion(request):
    return render(request, 'site_web/adhesion.html')


def galerie(request):
    images_galeries = ImageGalerie.objects.all()
    data = {
        'images': images_galeries
    }
    return render(request, 'site_web/galerie.html', data)


def about(request):
    return render(request, 'site_web/about.html')
