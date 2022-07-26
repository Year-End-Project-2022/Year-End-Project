import json

from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import ImageGalerie, Atelier
from local_user.forms import UserEditForm, CompetenceForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from local_user.models import Competence


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

@login_required
def utilisateur(request):
    try:
        user = request.user
        competences = user.competences
        print('Competence.objects.all().values_list')
        qs = Competence.objects.all().values_list('name', flat=True)
        print(qs)
        value = [item for item in qs]
        print('value: ')
        print(value)

        data = {
            'utilisateur': user,
            'competences': competences,
        }
    except user.DoesNotExist:
        return redirect('index')
    if request.user.is_authenticated:
        return render(request, 'site_web/utilisateur.html', data)
    else:
        return redirect('index')


@login_required
def edit_utilisateur(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        print('request :')
        print(request.POST)

        if 'competence' in request.POST and 'value' in request.POST and 0 < float(request.POST['value']) <= 5:
            competence = request.POST['competence']
            value = request.POST['value']
            request.user.competences[competence] = int(float(value) * 20)
            request.user.save()
        #  print({'competence': competence_form.competence, 'value': competence_form.value * 20})
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return HttpResponseRedirect('utilisateur')
        else:
            messages.error(request, 'Error to update profile')
            return HttpResponseRedirect('edit_utilisateur')

    else:
        user_form = UserEditForm(instance=request.user)
        competence_form = CompetenceForm()
        user = request.user
        competences = user.competences
        qs = Competence.objects.all().values_list('name', flat=True)
        competences_list = [item for item in qs]

        return render(request, 'site_web/utilisateur_edit.html', {
            'user_form': user_form,
            'competence_form': competence_form,
            'utilisateur': user,
            'competences': competences,
            'competences_list': competences_list,

        })
