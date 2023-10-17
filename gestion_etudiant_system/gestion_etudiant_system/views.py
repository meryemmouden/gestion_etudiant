from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponse
from app.EmailBackEnd import EmailBackEnd

from django.contrib import messages

from app.models import CustumUser


def BASE(request):
    return render(request,'base.html')


def CONNEXION(request):
    return render(request,'connexion.html')


def FAIRE_CONNEXION(request):
    if request.method =="POST":
      user=EmailBackEnd.authenticate(request,username=request.POST.get('email'), password=request.POST.get('password'),)
      if user!=None:
        login(request,user)
        user_type=user.user_type
        if user_type == '1' :
            return redirect("admin_home")
        elif user_type =="2" :
            return redirect("prof_feedback")
        elif user_type =="3" :
            return redirect("student_feedback")
        else:
            messages.error(request,'email ou mot de passe ne sont pas valides')
            return redirect('login')
      else:
          messages.error(request, 'email ou mot de passe ne sont pas valides')
          return redirect('login')


def FAIRE_DECONNEXION(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/')
def PROFILE(request):
    user=CustumUser.objects.get(id=request.user.id)

    context= {
        'user':user,
    }
    return render(request,'profile.html',context)

@login_required(login_url='/')
def MODIFIE_PROFIL(request):
    if request.method=="POST":
        photo_profil=request.FILES.get('profile_pic')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')

        password = request.POST.get('password')
        print(photo_profil)
        try:
            customuser=CustumUser.objects.get(id = request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name

            if password !=None and password != "" :
                customuser.set_password(password)
            if photo_profil !=None and photo_profil !="":
                customuser.photo_profil = photo_profil
            customuser.save()
            messages.success(request,'Votre profil a été mis à jour avec succés ! ')
            return redirect('profile')
        except:
                messages.error(request,'Echec de la mise à jour de votre profil')
    return render(request,'profile.html')