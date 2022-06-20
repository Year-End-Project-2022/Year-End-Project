from django.shortcuts import redirect, render
from .models import ImageGalerie, Atelier


def index(request):
    return render(request, 'site_web/index.html')


def news(request):
    return render(request, 'site_web/news.html')


def ateliers(request):
    all_ateliers = Atelier.objects.all()
    data = {
        'ateliers': all_ateliers
    }
    return render(request, 'site_web/atelier/ateliers.html', data)


def atelier(request, name):
    try:
        atelier_obj = Atelier.objects.get(titre=name)
        data = {
            'atelier': atelier_obj
        }
    except Atelier.DoesNotExist:
        return redirect('index')
    return render(request, 'site_web/atelier/atelier.html', data)


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

def utilisateur(request):
    try:
        user = {          
            'username': 'username',
            'password': 'admin',
            'email': 'test@test.fr',
            'first_name': 'Elie',
            'last_name': 'Moriceau',
            'competance': [{'name': 'css', 'value': 40}, {'name': 'Impression 3D', 'value': 40}, {'name': 'cnc', 'value': 65}, {'name': 'figma', 'value': 100}, {'name': 'css', 'value': 40}, {'name': 'Impression 3D', 'value': 40}, {'name': 'cnc', 'value': 65}, {'name': 'figma', 'value': 100}],
            'discord': 'discordName',
            'credit': 2,
            'img': 'https://st4.depositphotos.com/1012074/20946/v/450/depositphotos_209469984-stock-illustration-flat-isolated-vector-illustration-icon.jpg',
            'subscriptionDate': '22-02-1996'
        }
        
        data = {
            'utilisateur': user
        }
    except Atelier.DoesNotExist:
        return redirect('index')
    return render(request, 'site_web/utilisateur.html', data)
