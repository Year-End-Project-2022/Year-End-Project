from django.shortcuts import render, redirect
from .models import Atelier


def ateliers(request):
    all_ateliers = Atelier.objects.all()
    data = {
        'ateliers': all_ateliers
    }
    return render(request, 'atelier/ateliers.html', data)

def atelier(request, name):
    try:
        atelier_obj = Atelier.objects.get(titre=name)
        data = {
            'atelier': atelier_obj
        }
    except Atelier.DoesNotExist:
        return redirect('index')
    return render(request, 'atelier/atelier.html', data)
