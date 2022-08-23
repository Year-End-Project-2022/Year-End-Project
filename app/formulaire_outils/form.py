from django import forms
from local_user.models import LocalUser, Competence
from formulaire_outils.models import OutilsCnc


class OutilsCncCreateForm():

    duration = forms.IntegerField(min_value=0,max_value=480 required=True, label="Temps de reservation")
    date = forms.DateField(required=True, label="Date", widget=forms.TextInput(attrs={'placeholder': 'JJ/MM/AAAA'}))

    def save(self, request):
        outils_cnc = super(OutilsCncCreateForm, self).save(request)
        outils_cnc.user = self.cleaned_data['user']
        outils_cnc.outils_cnc = self.cleaned_data['outil_cnc']
        outils_cnc.date = self.cleaned_data['date']
        outils_cnc.duration = self.cleaned_data['duration']
        outils_cnc.save()
        return outils_cnc

class OutilsCncEditForm(forms.ModelForm):
    duration = forms.IntegerField(min_value=0,max_value=480 required=True, label="Temps de reservation")
    date = forms.DateField(required=True, label="Date", widget=forms.TextInput(attrs={'placeholder': 'JJ/MM/AAAA'}))
    
    class Meta:
        model = OutilsCnc
        fields = ['date', 'duration']
    
    def save(self, request):
        outils_cnc.date = self.cleaned_data['date']
        outils_cnc.duration = self.cleaned_data['duration']
        outils_cnc.save()
        return outils_cnc