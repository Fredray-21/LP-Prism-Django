"""
URL configuration for ArtSpectra project.

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
from django.urls import path
from appliArtSpectra import views
from django.conf.urls.static import static
from accounts.views import signup, logout_user,login_user, profil, artiste, artistes
from ArtSpectra import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.oeuvres, name='accueil'),
    path('oeuvres/', views.oeuvres, name='oeuvres'),
    path('oeuvres/<str:slug>/<int:idOeuvre>/', views.oeuvre, name='oeuvre'),
    path('oeuvres/<str:slug>/', views.typeOeuvre, name='typeOeuvre'),
    path('profil/', profil, name='profil'),
    path('artistes/<str:username>/', artiste, name='artiste'),
    path('artistes/', artistes, name='artistes'),


    path('oeuvre/<int:idOeuvre>/modifier/', views.modifierOeuvre, name='modifierOeuvre'),
    path('oeuvre/<int:idOeuvre>/supprimer/', views.supprimerOeuvre, name='supprimerOeuvre'),
    path('ajouterOeuvre/', views.ajouterOeuvre, name='ajouterOeuvre'),


    path('signup/', signup, name='signup'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),

    path('panier/', views.panier, name='panier'),
    path('ajouter-au-panier/<int:oeuvre_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('supprimer-du-panier/<int:panieroeuvre_id>/', views.supprimer_du_panier, name='supprimer_du_panier'),


    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='accounts/password_reset.html',
             email_template_name='accounts/password_reset_email.html'),
         name='password_reset'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)