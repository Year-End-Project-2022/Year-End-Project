from datetime import date
from django.shortcuts import render, redirect
from .models import Atelier, Seance, Session
from django.contrib.auth.decorators import login_required



def ateliers(request):
    all_ateliers = Atelier.objects.all()
    data = {
        'ateliers': all_ateliers
    }
    return render(request, 'atelier/ateliers.html', data)

def atelier(request, name):
    today = date.today()
    try:
        atelier_obj = Atelier.objects.get(titre=name)
        all_seance_obj = Seance.objects.filter(atelier=atelier_obj)
        seance_obj = []
        for i in range(0, all_seance_obj.count(), 1) :
            session_past = Session.objects.filter(seance=all_seance_obj[i], date__lt=today)
            session_futur = Session.objects.filter(seance=all_seance_obj[i], date__gte=today)
            if session_past.count() == 0 and session_futur.count() != 0:
                tempTab = []
                tempTab.append(all_seance_obj[i])
                tempTab.append(session_futur)
                seance_obj.append(tempTab)

        interrested = False
        listInterested = atelier_obj.presonne_interesse.values()
        if request.user.is_authenticated :
            for interUser in listInterested :
                if interUser.get("id") == request.user.id :
                    interrested = True
        data = {
            'atelier': atelier_obj,
            'interested': interrested,
            'seances': seance_obj,
        }
    except Atelier.DoesNotExist:
        return redirect('index')
    return render(request, 'atelier/atelier.html', data)

@login_required
def interested(request,name):
    try:
        IsInterested = False
        atelier_obj = Atelier.objects.get(titre=name)
        listInterested = atelier_obj.presonne_interesse.values()
        for interUser in listInterested :
            if interUser.get("id") == request.user.id :
                IsInterested = True
        if IsInterested :
            atelier_obj.presonne_interesse.remove(request.user)
        else :
            atelier_obj.presonne_interesse.add(request.user)
    except Atelier.DoesNotExist:
        return redirect('index')
    return redirect('atelier',name)