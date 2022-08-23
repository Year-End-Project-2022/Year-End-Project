from datetime import date, datetime
import json

from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect

from atelier.models import Session
from .calendarUtil import Calendar
from .models import ImageGalerie
from local_user.forms import UserEditForm, CompetenceForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.utils.safestring import mark_safe

from local_user.models import Competence


def index(request):
    return render(request, 'site_web/index.html')


def news(request):
    return render(request, 'site_web/news.html')


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
        user_form = UserEditForm(request.POST, request.FILES, instance=request.user)
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

@login_required
def delete_competence(request):
    if request.method == 'GET':
        competence = request.GET.get('competence')
        del request.user.competences[competence]
        request.user.save()
        messages.success(request, 'Your competence is updated successfully')
    return HttpResponseRedirect('edit_utilisateur')



class CalendarView(generic.ListView):
    model = Session
    template_name = 'site_web/atelier/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()