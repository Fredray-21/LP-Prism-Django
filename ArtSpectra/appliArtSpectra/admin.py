from django.contrib import admin
from appliArtSpectra.models import Oeuvre
from accounts.models import Shopper

# Register your models here.
admin.site.register(Oeuvre)
admin.site.register(Shopper)