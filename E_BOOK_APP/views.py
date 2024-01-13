from ast import List
import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from E_BOOK_APP.models import *
from E_BOOK_APP.forms import *
from django.db.models import Avg
from django.db.models import F,Q
# Create your views here.
is_index=False

def index(request):
    is_index=True
    categories=categorie.objects.all()
    Auteurs_pop=[]
    moyenne=0
    
    Tous_Les_Livres=Livre.objects.all()
    nb=Tous_Les_Livres.count()
    for livre in Tous_Les_Livres:
        moyenne+=livre.score/nb
    print(moyenne)
    populaires=Livre.objects.filter(score__gte=moyenne-2)
  
    ensemble=[]
     
    for livre in populaires:
        if livre.Aut_is_User :
            ensemble.append(livre.Aut_User)
    ensembleSet=set(ensemble)
    Auteurs_pop=list(ensembleSet)
    MesLectures = Lecture.objects.filter(utilisateur__id=request.user.id).order_by('date')[:3]
    return render(request,'E_BOOK_APP/index.html',context={
     "Auteurs_pop":Auteurs_pop,
     "Tous_Les_Livres":Tous_Les_Livres,
     "categories":categories,
     "is_index":is_index,
     "lectures":MesLectures,
     "Livres_Populaires":populaires})
    
    
def publier(request):
    MesLectures = Lecture.objects.filter(utilisateur__id=request.user.id).order_by('date')[:3]
    global is_index
    categories=categorie.objects.all()
    is_valid=False
    post=False
    if request.method == 'POST':
        post=True
        form = LivreForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()
            is_valid=True
            return render(request, 'E_BOOK_APP/publier.html',context={'is_valid':is_valid,'post':post,"categories":categories,"lectures":MesLectures})
        else :
            print(form.errors)
            return render(request, 'E_BOOK_APP/publier.html',context={'is_valid':is_valid,'post':post,"categories":categories,"lectures":MesLectures})
    else:
        form = LivreForm()
    return render(request, 'E_BOOK_APP/publier.html', {'form': form,'is_valid':is_valid,"categories":categories,"lectures":MesLectures,"is_index":is_index,'post':post})
        


def incrementer_score(id):
    livre = Livre.objects.get(id=id)
    livre.score = F('score') + 1
    livre.save()
def Livre_detail(request,id):
    MesLectures = Lecture.objects.filter(utilisateur__id=request.user.id).order_by('date')[:3]
    global is_index
    commentaires=Commentaire.objects.filter(id_livre=id)
    categories=categorie.objects.all()
    # Obtenir la date d'aujourd'hui
    aujourdhui = date.today()

    # Définir un délai de 3 jours pour considérer un livre comme récent
    delai = timedelta(days=3)

    # Filtrer les livres dont la date est supérieure ou égale à aujourd'hui - délai
    Livres_recents = Livre.objects.filter(date__gte=aujourdhui - delai)
    livre=get_object_or_404(Livre,id=id)
    nb_com=commentaires.count()
    if request.method == 'POST':
        form = CommentForm(request.POST,request.FILES)
        
        if form.is_valid():
            incrementer_score(id)
            form.save()
            return render(request, 'E_BOOK_APP/detail-read.html', {"categories":categories,"lectures":MesLectures,"is_index":is_index,"livre":livre,"Livres_recents":Livres_recents,"Commentaires":commentaires,"nb_com":nb_com})
        else :
            print(form.errors)
            return render(request, 'E_BOOK_APP/detail-read.html', {"categories":categories,"lectures":MesLectures,"is_index":is_index,"livre":livre,"Livres_recents":Livres_recents,"Commentaires":commentaires,"nb_com":nb_com})
    else:
        form = LivreForm()
        incrementer_score(id)
    return render(request, 'E_BOOK_APP/detail-read.html', {"categories":categories,"lectures":MesLectures,"is_index":is_index,"livre":livre,"Livres_recents":Livres_recents,"Commentaires":commentaires,"nb_com":nb_com})



def rechercher(request):
    MesLectures = Lecture.objects.filter(utilisateur__id=request.user.id).order_by('date')[:3]
    global is_index
    categories=categorie.objects.all()
    sujet=request.GET.get("search")
    categorieSearch=request.GET.get("categorie")
    Livres_recherche = Livre.objects.filter(Q(categorie__nom_categorie__icontains=categorieSearch) & (Q(Titre__icontains=sujet) | Q(Auteur__icontains=sujet))) 

    return render(request,'E_BOOK_APP/Resultat.html',{"categories":categories,"lectures":MesLectures,"is_index":is_index,"Livres_recherche":Livres_recherche,"sujet":sujet,"categorie":categorieSearch})

def Commenter(request , id):
    MesLectures = Lecture.objects.filter(utilisateur__id=request.user.id).order_by('date')[:3]
    global is_index
    commentaires=Commentaire.objects.filter(id_livre=id)
    categories=categorie.objects.all()
    # Obtenir la date d'aujourd'hui
    aujourdhui = date.today()

    # Définir un délai de 3 jours pour considérer un livre comme récent
    delai = timedelta(days=3)

    # Filtrer les livres dont la date est supérieure ou égale à aujourd'hui - délai
    Livres_recents = Livre.objects.filter(date__gte=aujourdhui - delai)
    livre=get_object_or_404(Livre,id=id)
    nb_com=commentaires.count()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            form.save()
            return render(request, 'E_BOOK_APP/detail-read.html', {"categories":categories,"lectures":MesLectures,"is_index":is_index,"livre":livre,"Livres_recents":Livres_recents,"Commentaires":commentaires,"nb_com":nb_com})
        else :
            print(form.errors)
            return render(request, 'E_BOOK_APP/detail-read.html', {"categories":categories,"lectures":MesLectures,"is_index":is_index,"livre":livre,"Livres_recents":Livres_recents,"Commentaires":commentaires,"nb_com":nb_com})
    else:
        form = LivreForm()
    return render(request, 'E_BOOK_APP/detail-read.html', {"categories":categories,"lectures":MesLectures,"is_index":is_index,"livre":livre,"Livres_recents":Livres_recents,"Commentaires":commentaires,"nb_com":nb_com})


def MesLivres(request,id):
    MesLectures = Lecture.objects.filter(utilisateur__id=request.user.id).order_by('date')[:3]
    global is_index
    categories=categorie.objects.all()
    MesLivres=Livre.objects.filter(Aut_User__id=id).order_by('date')
    #MesLivres=Livre.objects.all()
    return render(request, 'E_BOOK_APP/MesLivres.html', {"categories":categories,"lectures":MesLectures,"is_index":is_index,"MesLivres":MesLivres})

def MesLectures(request,id):
    mesLectures = Lecture.objects.filter(utilisateur__id=request.user.id).order_by('date')[:3]
    global is_index
    categories=categorie.objects.all()
    MesLectures=Lecture.objects.filter(utilisateur__id=id).order_by('date')
    #MesLivres=Livre.objects.all()
    return render(request, 'E_BOOK_APP/MesLectures.html', {"categories":categories,"lectures":mesLectures,"is_index":is_index,"MesLectures":MesLectures})

def AjoutLectures(request,id):
    
    lecture=Lecture(utilisateur=request.user,livre=get_object_or_404(Livre,id=id))
    lecture.save()
      

def SupprimerLecture(request , id):
    lecture=get_object_or_404(Lecture,id=id)
    if lecture.utilisateur == request.user:
      lecture.delete()
      return redirect("MesLectures",request.user.id) 
    else:
      return render(request,"E_BOOK_APP/404.html")

def SupprimerLivre(request, id):
    livre=get_object_or_404(Livre,id=id)
    if livre.Aut_User == request.user:
      livre.delete()
      return redirect("MesLivress",request.user.id) 
    else:
        return render(request,"E_BOOK_APP/404.html")
    
    

def LivresAuteur(request,id):
    MesLectures = Lecture.objects.filter(utilisateur__id=request.user.id).order_by('date')[:3]
    global is_index
    categories=categorie.objects.all()
    Auteur=get_object_or_404(Utilisateur,id=id)
    Livres_recherche = Livre.objects.filter(Aut_User__id = int(id)) 

    return render(request,'E_BOOK_APP/Auteur.html',{"categories":categories,"lectures":MesLectures,"is_index":is_index,"Livres_Auteur":Livres_recherche,"categorie":categories,"Auteur":Auteur})

def checkout(request,id):
    MesLectures = Lecture.objects.filter(utilisateur__id=request.user.id).order_by('date')[:3]
    livre=get_object_or_404(Livre,id=id)
    return render(request,"E_BOOK_APP/checkout.html",{"livre":livre})

def premium(request):
    MesLectures = Lecture.objects.filter(utilisateur__id=request.user.id).order_by('date')[:3]
    return render(request,"E_BOOK_APP/premium.html")


def error_404_view(request, exception):
    # Votre logique pour gérer l'erreur 404
    return render(request, '404.html', {}, status=404)
def error_500_view(request):
    # Votre logique pour gérer l'erreur 404
    return render(request, '404.html', {}, status=500)