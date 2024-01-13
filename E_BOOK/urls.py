"""
URL configuration for E_BOOK project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from E_BOOK import settings
from E_BOOK_APP.views import *
from Accounts.views import *

handler404 = 'E_BOOK_APP.views.error_404_view'
handler500 = 'E_BOOK_APP.views.error_500_view'
urlpatterns = [
    path('',index,name='index'),
    path('admin/', admin.site.urls),
    path('publier',publier,name='publier'),
    path('Livre/<str:id>',Livre_detail,name='Livre_detail'), # type: ignore
    path('rechercher/',rechercher,name='rechercher'),
    path('register/',singup,name='register'),
    path('logout/',Logout,name='logout'),
    path('login/',login_user,name='login'),
    path('commenter/<str:id>',Commenter,name='commenter'), # type: ignore
    path('MesLivres/<str:id>',MesLivres,name='MesLivres'), # type: ignore
    path('MesLectures/<str:id>',MesLectures,name='MesLectures'),
    path('AjoutLectures/<str:id>',AjoutLectures,name='AjoutLectures'), # type: ignore
    path('SupprimerLecture/<str:id>',SupprimerLecture,name='SupprimerLecture'),# type: ignore
    path('SupprimerLivre/<str:id>',SupprimerLivre,name='SupprimerLivre'),
    path('LivresAuteur/<str:id>',LivresAuteur,name='LivresAuteur'),
    path('profile/',profileUser,name='profileUser'),
    path('buy/<str:id>',checkout,name='buy'),
    path('premium/',premium,name='premium')
    
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
