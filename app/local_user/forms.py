from allauth.account.forms import SignupForm
from django import forms


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