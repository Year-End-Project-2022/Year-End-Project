from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import ImageGalerie, Atelier
from local_user.forms import UserEditForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
        userTest = {
            'username': 'username',
            'password': 'admin',
            'email': 'test@test.fr',
            'first_name': 'Elie',
            'last_name': 'Moriceau',
            'competance': [{'name': 'css', 'value': 40}, {'name': 'Impression 3D', 'value': 40},
                           {'name': 'cnc', 'value': 65}, {'name': 'figma', 'value': 100}, {'name': 'css', 'value': 40},
                           {'name': 'Impression 3D', 'value': 40}, {'name': 'cnc', 'value': 65},
                           {'name': 'figma', 'value': 100}],
            'discord': 'discordName',
            'credit': 2,
            'img': 'https://st4.depositphotos.com/1012074/20946/v/450/depositphotos_209469984-stock-illustration-flat-isolated-vector-illustration-icon.jpg',
            'subscriptionDate': '22-02-1996'
        }
        user = request.user

        data = {
            'utilisateur': user
        }
    except Atelier.DoesNotExist:
        return redirect('index')
    if request.user.is_authenticated:
        return render(request, 'site_web/utilisateur.html', data)
    else:
        return redirect('index')


@login_required
def edit_utilisateur(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        print('POST')
        print(request.POST)
        print(user_form.is_valid())
        if user_form.is_valid():
            print('valide')
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return HttpResponseRedirect('utilisateur')
        else:
            messages.error(request, 'Error to update profile')
            return HttpResponseRedirect('edit_utilisateur')

    else:
        user_form = UserEditForm(instance=request.user)
        user = request.user
        return render(request, 'site_web/utilisateur_edit.html', {'user_form': user_form, 'utilisateur': user})
