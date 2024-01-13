from email.policy import default
from django.db import models
from django.urls import reverse
from datetime import date, datetime, timedelta

from sympy import true
from Accounts.models import Utilisateur
# Create your models here.

class categorie(models.Model):
    nom_categorie=models.CharField(max_length=200,primary_key=True)
    def __str__(self):
        return self.nom_categorie


class Commentaire(models.Model):
    id=models.IntegerField(unique=True,auto_created=True,editable=False,primary_key=True)
    id_livre=models.IntegerField()
    nom=models.CharField(max_length=200)
    posteur=models.ForeignKey(Utilisateur,on_delete=models.CASCADE,null=True,blank=True)
    date=models.DateTimeField(auto_now=True,auto_created=True)
    description=models.TextField(blank=True, null=True)
    

class Livre(models.Model):
    
    id=models.IntegerField(unique=True,auto_created=True,editable=False,primary_key=True)
    is_premium=models.BooleanField(default=False)
    en_vente=models.BooleanField(default=False)
    AdminCom=models.TextField(default="AUCUN COMMENTAIRE DE L'ADMINISTRATEUR POUR LE MOMENT",blank=True,null=True)
    recommande=models.BooleanField(default=False)
    categorie=models.ForeignKey(categorie,on_delete=models.CASCADE)
    Titre= models.CharField(max_length=228)
    Auteur=models.CharField(max_length=128)
    Aut_User=models.ForeignKey(Utilisateur,on_delete=models.CASCADE,null=True,blank=True)
    description=models.TextField(blank=True, null=True)
    date=models.DateTimeField(auto_created=True, default=datetime.now())
    image2=models.ImageField(upload_to="Images_Livres",blank=True,null=True) #je dois renseigner une image par defaut ici 
    image1=models.ImageField(upload_to="Images_Livres")      #image du livre
    score= models.IntegerField(default=0)
    prix=models.FloatField(default=0,null=True, blank=True) #on va recuperer la ou le prix n'est pas zero
    Aut_is_User=models.BooleanField(default=False)
    pdf=models.FileField(upload_to="livres_pdf")
    
    
    
    @property
    def is_new(self):
        # Retourne True si self.date est dans les trois derniers jours, False sinon
        today = date.today()
        margin = timedelta(days=3)
        return today - margin <= self.date.date() <= today
    #methode qui permet de representer notre livre sous forme de chaine dans l'interface d'admin
    def __str__(self) :
        return f"Livre : {self.id} | Titre : {self.Titre} | Par:  {self.Auteur} | Utilisateur ? : {self.Aut_is_User} | Categorie : {self.categorie} | le : {self.date} "
    def get_absolute_url(self):
        return reverse("Livre_detail", kwargs={"id": self.id})

class Lecture(models.Model):
    id=models.IntegerField(unique=True,auto_created=True,editable=False,primary_key=True)
    date=models.DateTimeField(auto_created=True,null=True,blank=True,auto_now=True)
    utilisateur=models.ForeignKey(Utilisateur,on_delete=models.CASCADE,null=True,blank=True)
    livre=models.ForeignKey(Livre,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f"Lecture de {self.livre} par {self.utilisateur} "