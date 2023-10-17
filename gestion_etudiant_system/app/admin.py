from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import *


class UserModel(UserAdmin):
    list_display = ['username' , 'user_type']

admin.site.register(CustumUser,UserModel)
admin.site.register(Groupe)
admin.site.register(Anne_de_session)
admin.site.register(Etudiant)
admin.site.register(Professeur)
admin.site.register(Matiere)
admin.site.register(Prof_Notification)
admin.site.register(Etudiant_Notification)
admin.site.register(Professeur_conge)
admin.site.register(Prof_message)
admin.site.register(Etudiant_message)
admin.site.register(Abscence)
admin.site.register(Abscence_Raport)
admin.site.register(EtudiantResultat)
