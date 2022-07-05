from allauth.account.forms import SignupForm
from django import forms

from local_user.models import LocalUser


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, required=True, label="Prénom")
    last_name = forms.CharField(max_length=30, required=True, label="Nom")

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(label="Prénom :")
    last_name = forms.CharField(label="Nom :")
    username = forms.CharField(label="Username :")
    date_naissance = forms.DateField(label="Date de naissance :", required=False)
    pseudo_discord = forms.CharField(label="Discord :", max_length=100, required=False)
    github = forms.CharField(label="Github :", max_length=100, required=False)
    img = forms.URLField(label="Importer avatar", required=False)

    class Meta:
        model = LocalUser
        fields = ['first_name', 'last_name', 'username', 'date_naissance', 'pseudo_discord', 'github', 'img']
