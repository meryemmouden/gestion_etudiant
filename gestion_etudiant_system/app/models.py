from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustumUser(AbstractUser):
    USER=(
        (1,'ADMIN'),
        (2,'PROFESSEUR'),
        (3,'ETUDIANT'),
    )
    user_type=models.CharField(choices=USER,max_length=50,default=1)
    photo_profil=models.ImageField(upload_to='media/photo_profil')


class Groupe(models.Model):
    nom=models.CharField(max_length=50)
    cree_a=models.DateTimeField(auto_now_add=True)
    modifier_a=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

class Anne_de_session(models.Model):
    debut_session=models.CharField(max_length=100)
    fin_session=models.CharField(max_length=100)

    def __str__(self):
        return self.debut_session + " To " + self.fin_session

class Etudiant(models.Model):
    admin=models.OneToOneField(CustumUser,on_delete=models.CASCADE)
    adresse=models.TextField()
    sex=models.CharField(max_length=100)
    groupe_id = models.ForeignKey(Groupe, on_delete=models.DO_NOTHING)
    anne_de_session=models.ForeignKey(Anne_de_session, on_delete=models.DO_NOTHING)
    cree_a=models.DateTimeField(auto_now_add=True)
    modifier_a=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name

class Professeur(models.Model):
    admin = models.OneToOneField(CustumUser,on_delete=models.CASCADE)
    addresse = models.TextField()
    sex = models.CharField(max_length=100)
    cree_a = models.DateTimeField(auto_now_add=True)
    modifier_a = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.username

class Matiere(models.Model):
    nom = models.CharField(max_length=100)
    groupe= models.ForeignKey(Groupe,on_delete=models.CASCADE)
    professeur= models.ForeignKey(Professeur,on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Prof_Notification(models.Model):
    prof_id= models.ForeignKey(Professeur, on_delete=models.CASCADE)
    message=models.TextField()
    cree_a=models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(null=True,default=0)

    def __str__(self):
        return self.prof_id.admin.first_name


class Etudiant_Notification(models.Model):
    etudiant_id= models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    message=models.TextField()
    cree_a=models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(null=True,default=0)

    def __str__(self):
        return self.etudiant_id.admin.first_name


class Professeur_conge(models.Model):
    professeur_id= models.ForeignKey(Professeur, on_delete=models.CASCADE)
    data=models.CharField(max_length=100)
    message=models.TextField()
    status = models.IntegerField(default=0)
    cree_a=models.DateTimeField(auto_now_add=True)
    modifie_a = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.professeur_id.admin.first_name + self.professeur_id.admin.last_name



class Prof_message(models.Model):
     prof_id = models.ForeignKey(Professeur, on_delete=models.CASCADE)
     message= models.TextField()
     reponse_message = models.TextField()
     status = models.IntegerField(default=0)
     cree_a = models.DateTimeField(auto_now_add=True)
     modifie_a = models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return self.prof_id.admin.first_name + self.prof_id.admin.last_name


class Etudiant_message(models.Model):
     etudiant_id = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
     message= models.TextField()
     message_reponse = models.TextField()
     status=models.IntegerField(default=0)
     cree_a= models.DateTimeField(auto_now_add=True)
     modifie_a = models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return self.etudiant_id.admin.first_name + self.etudiant_id.admin.last_name

class Abscence(models.Model):
    matiere_id=models.ForeignKey(Matiere,on_delete=models.DO_NOTHING)
    abscence_data=models.DateField()
    anne_session_id=models.ForeignKey(Anne_de_session,on_delete=models.DO_NOTHING)
    cree_a = models.DateTimeField(auto_now_add=True)
    modifie_a = models.DateTimeField(auto_now_add=True)


    def __str__(self):
     return self.matiere_id.nom

class Abscence_Raport(models.Model):
    etudiant_id=models.ForeignKey(Etudiant,on_delete=models.DO_NOTHING)
    abscence_id=models.ForeignKey(Abscence,on_delete=models.CASCADE)
    cree_a = models.DateTimeField(auto_now_add=True)
    modifie_a = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.etudiant_id.admin.first_name



class EtudiantResultat(models.Model):
    etudiant_id=models.ForeignKey(Etudiant,on_delete=models.CASCADE)
    matiere_id = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    controle_note=models.IntegerField()
    exam_note=models.IntegerField()

    cree_a = models.DateTimeField(auto_now_add=True)
    modifie_a= models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.etudiant_id.admin.first_name

