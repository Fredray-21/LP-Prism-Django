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
from accounts.views import signup, logout_user,login_user
from ArtSpectra import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.oeuvres, name='accueil'),
    path('oeuvres/', views.oeuvres, name='oeuvres'),
    path('oeuvres/<str:slug>/<int:idOeuvre>/', views.oeuvre, name='oeuvre'),
    path('oeuvres/<str:slug>/', views.typeOeuvre, name='typeOeuvre'),


    path('signup/', signup, name='signup'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
