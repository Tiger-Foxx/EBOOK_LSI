from django import forms
from E_BOOK_APP.models import *


class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['Titre','categorie', 'Auteur','Aut_User','image1','image2','prix','Aut_is_User','description','pdf']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields=['nom','description','posteur','id_livre']
        
    