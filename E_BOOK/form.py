from django import forms

from Accounts.models import Utilisateur 

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields=['username','email','telephone','profil']