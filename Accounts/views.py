from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import get_user_model,login,logout,authenticate
import django.contrib.auth.models
from Accounts.models import *
from E_BOOK.form import ProfileForm

# Create your views here.
User=get_user_model()
from django.http import JsonResponse # Importer la classe JsonResponse

def singup(request):
    
    if request.method == 'POST':
        # traiter le formulaire
        passwordConfirm =request.POST.get("confpassword")
        password =request.POST.get("password")
        name =request.POST.get("nom")
        telephone=request.POST.get("telephone")
        email=request.POST.get("email")
        profil=request.FILES.get("profil")
        Remember =request.POST.get("remember-me")
        if password==passwordConfirm:
            try:
              user=User.objects.create_user(telephone=telephone,username=name,password=password,profil=profil,email=email) # type: ignore
              login(request,user)
              request.session.set_expiry(1209600) # 2 weeks
              if not Remember:
                print("not remember")

                request.session.set_expiry(0)
            except:
                return JsonResponse({"success": False, "message": " l'utilisateur existe deja."}) # Renvoyer une réponse JSON avec un indicateur d'échec et un message d'erreur

            
        #apres inscription on le redirige
            return JsonResponse({"success": True, "redirect_url": "/"}) # Renvoyer une réponse JSON avec un indicateur de succès et l'URL de redirection
        else:
            return JsonResponse({"success": False, "message": "Les mots de passe ne correspondent pas."}) # Renvoyer une réponse JSON avec un indicateur d'échec et un message d'erreur
    else :
        return render(request,"Accounts/register.html")

    
def Logout(request):
    logout(request)
    return render(request,"Accounts/register.html")


def login_user(request):
    if request.method == 'POST':
        # conecter l'utilisateur
        name = request.POST.get("nom")
        print(name + "est le nom")
        password =request.POST.get("password")
        Remember =request.POST.get("remember-me")
        print("le mdp est : "+password)
        
        user=authenticate(username=name, password=password)
        if user:
            
            login(request,user)
            request.session.set_expiry(1209600) # 2 weeks
            if not Remember:
                print("not remember")
                 
                print(Remember)
                print(type(Remember))
                print("ok")
                request.session.set_expiry(0)
            return JsonResponse({"success": True, "redirect_url": "/"})#apres inscription on le redirige
        else:    
            return JsonResponse({"success": False, "message": "Nom d'utilisateur ou mot de passe incorrect !"}) # Renvoyer une réponse JSON avec un indicateur d'échec et un message d'erreur

    else :
        return render(request,"Accounts/register.html")
    
def profileUser(request):
    is_valid=False
    if request.method=="POST":
        
        utilisateur=get_object_or_404(Utilisateur,id=request.user.id)
        form = ProfileForm(request.POST,request.FILES,instance=utilisateur)
        if form.is_valid():
            
            form.save()
            is_valid=True
            return redirect("index")
        else:
            is_valid=False
            print(form.errors)
            return render(request,"Accounts/profile.html",{"is_valid":is_valid})
    
    else:    
        return render(request,"Accounts/profile.html",{"is_valid":True})