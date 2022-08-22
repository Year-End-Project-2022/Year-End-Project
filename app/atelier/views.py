from django.shortcuts import render, redirect
from .models import Atelier
from django.contrib.auth.decorators import login_required


def ateliers(request):
    all_ateliers = Atelier.objects.all()
    data = {
        'ateliers': all_ateliers
    }
    return render(request, 'atelier/ateliers.html', data)

def atelier(request, name):
    try:
        atelier_obj = Atelier.objects.get(titre=name)
        interrested = False
        listInterested = atelier_obj.presonne_interesse.values()
        if request.user.is_authenticated :
            for interUser in listInterested :
                if interUser.get("id") == request.user.id :
                    interrested = True
        data = {
            'atelier': atelier_obj,
            'interested': interrested,
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