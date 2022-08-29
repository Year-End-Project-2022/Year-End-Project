from allauth.account.forms import SignupForm
from django import forms
from local_user.models import LocalUser, Competence


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, required=True, label="Prénom")
    last_name = forms.CharField(max_length=30, required=True, label="Nom")
    date_naissance = forms.DateField(required=True, label="Date de naissance",
                                    widget=forms.TextInput(
                                        attrs={'placeholder': 'JJ/MM/AAAA'}))

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.date_naissance = self.cleaned_data['date_naissance']
        user.save()
        return user


class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(label="Prénom :")
    last_name = forms.CharField(label="Nom :")
    username = forms.CharField(label="Username :")
    date_naissance = forms.DateField(label="Date de naissance :", required=False)
    pseudo_discord = forms.CharField(label="Discord :", max_length=100, required=False)
    github = forms.CharField(label="Github :", max_length=100, required=False)
    photo = forms.ImageField(required=False)

    class Meta:
        model = LocalUser
        fields = ['first_name', 'last_name', 'username', 'date_naissance', 'pseudo_discord', 'github', 'photo']


class CompetenceForm(forms.Form):
    qs = Competence.objects.all().values_list('name', flat=True)

    competence_list = ['CSS']
    competence = forms.ChoiceField(choices=competence_list, label='Compétence :')
    value = forms.IntegerField(min_value=0, max_value=5, label='Niveau (entre 1 à 5):', required=False)
