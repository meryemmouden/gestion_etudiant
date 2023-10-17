from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from app.models import Groupe, Anne_de_session, CustumUser, Etudiant, Matiere, Professeur, \
    Abscence, Abscence_Raport, Prof_message, Etudiant_message, Professeur_conge, Prof_Notification, \
    Etudiant_Notification


@login_required(login_url='/')
def HOME(request):
    etudiant_count=Etudiant.objects.all().count()
    prof_count = Professeur.objects.all().count()
    groupe_count = Groupe.objects.all().count()
    matiere_count=Matiere.objects.all().count()

    student_gender_male=Etudiant.objects.filter(sex='Garcon').count()
    student_gender_female = Etudiant.objects.filter(sex='Fille').count()

    context={
        'student_count':etudiant_count,
        'prof_count':prof_count,
        'groupe_count':groupe_count,
        'matiere_count':matiere_count,
        'student_gender_male':student_gender_male,
        'student_gender_female':student_gender_female ,
    }
    return render(request,'Admin/home.html',context)



@login_required(login_url='/')
def ADD_STUDENT(request):
    groupe = Groupe.objects.all()
    session_year = Anne_de_session.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        groupe_id = request.POST.get('groupe_id')
        session_year_id = request.POST.get('session_year_id')

        if CustumUser.objects.filter(email=email).exists():
           messages.warning(request,'Ce email est deja pris')
           return redirect('ajouter_etudiant')
        if CustumUser.objects.filter(username=username).exists():
           messages.warning(request,'Username est deja pris')
           return redirect('ajouter_etudiant')
        else:
            user = CustumUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                photo_profil= profile_pic,
                user_type = 3
            )
            user.set_password(password)
            user.save()

            groupe= Groupe.objects.get(id=groupe_id)
            session_year = Anne_de_session.objects.get(id=session_year_id)

            etudiant= Etudiant(
                admin = user,
                adresse=address,
                anne_de_session = session_year,
                groupe_id = groupe,
                sex = gender,
            )
            etudiant.save()
            messages.success(request, user.first_name + "  " + user.last_name + " est ajouté avec succès !")
            return redirect('ajouter_etudiant')



    context = {
        'groupe':groupe,
        'session_year':session_year,
    }

    return render(request,'Admin/ajouter_etudiant.html',context)

@login_required(login_url='/')
def VIEW_STUDENT(request):
    student = Etudiant.objects.all()

    context = {
        'student':student,
    }
    return render(request,'Admin/voir_etudiant.html',context)

@login_required(login_url='/')
def EDIT_STUDENT(request,id):
    student = Etudiant.objects.filter(id = id)
    groupe = Groupe.objects.all()
    session_year = Anne_de_session.objects.all()

    context = {
        'student':student,
        'groupe':groupe,
        'session_year':session_year,
    }
    return render(request,'Admin/edit_etudiant.html',context)

@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        print(student_id)
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        groupe_id = request.POST.get('groupe_id')
        session_year_id = request.POST.get('session_year_id')

        user = CustumUser.objects.get(id = student_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.photo_profil = profile_pic
        user.save()

        student = Etudiant.objects.get(admin = student_id)
        student.adresse = address
        student.sex = gender

        groupe = Groupe.objects.get(id = groupe_id)
        student.groupe_id = groupe

        session_year = Anne_de_session.objects.get(id = session_year_id)
        student.anne_de_session = session_year

        student.save()
        messages.success(request,'mis à jour avec succès !')
        return redirect('voir_student')

    return render(request,'Admin/edit_etudiant.html')


@login_required(login_url='/')
def DELETE_STUDENT(request,admin):
    student = CustumUser.objects.get(id = admin)
    student.delete()
    messages.success(request,'suppression avec succès!')
    return redirect('voir_student')


@login_required(login_url='/')
def ADD_GROUPE(request):

    if request.method == "POST":
        groupe_name = request.POST.get('groupe_name')

        groupe = Groupe(
            nom= groupe_name,
        )
        groupe.save()
        messages.success(request,'groupe est ajouté avec succès ')


        return redirect('ajouter_groupe')

    return render(request,'Admin/ajouter_groupe.html')


@login_required(login_url='/')
def VIEW_GROUPE(request):
    groupe = Groupe.objects.all()
    context = {
        'groupe': groupe,
    }
    return render(request, 'Admin/voir_groupe.html', context)


@login_required(login_url='/')
def EDIT_GROUPE(request,id):
    groupe = Groupe.objects.get(id = id)
    context = {
        'groupe': groupe,
    }
    return render(request, 'Admin/edit_groupe.html', context)


@login_required(login_url='/')
def UPDATE_GROUPE(request):
    if request.method == "POST":
        name = request.POST.get('name')
        groupe_id =request.POST.get('groupe_id')
        groupe = Groupe.objects.get(id = groupe_id)
        groupe.nom=name
        groupe.save()
        messages.success(request, 'groupe est modifié avec succès ')
        return redirect("view_groupe")

    return render(request, 'Admin/edit_groupe.html')

@login_required(login_url='/')
def DELETE_GROUPE(request,id):
    groupe = Groupe.objects.get(id=id)
    groupe.delete()
    messages.success(request,'groupe est supprimé avec succès')

    return redirect('view_groupe')

@login_required(login_url='/')
def ADD_PROF(request):
    if request.method == "POST":

        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        if CustumUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email est déja pris')
            return redirect('add_prof')
        if CustumUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username est déja pris')
            return redirect('add_prof')
        else:
            user = CustumUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                photo_profil=profile_pic,
                user_type=2
            )
            user.set_password(password)
            user.save()

            prof=Professeur(
                admin=user,
                addresse =address,
                sex=gender,
            )
            prof.save()
            messages.success(request, user.first_name + "  " +"  " + user.last_name + " est ajouté avec succès ")
            return redirect('add_prof')
    return render(request, 'Admin/ajouter_prof.html')


@login_required(login_url='/')
def VIEW_PROF(request):
    prof = Professeur.objects.all()
    context = {
        'professeur': prof,
    }
    return render(request, 'Admin/voir_prof.html',context)

@login_required(login_url='/')
def EDIT_PROF(request,id):
    prof = Professeur.objects.get(id =id)
    context = {
        'professeur': prof,
    }
    return render(request, 'Admin/edit_prof.html',context)


@login_required(login_url='/')
def UPDATE_PROF(request):
    if request.method == "POST":
        prof_id=request.POST.get('prof_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        user=CustumUser.objects.get(id = prof_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.photo_profil = profile_pic
        user.save()
        prof = Professeur.objects.get(admin=prof_id)
        prof.addresse = address
        prof.sex = gender

        prof.save()

        messages.success(request, 'mis à jour avec succès !')
        return redirect('view_prof')

    return render(request, 'Admin/edit_prof.html')

@login_required(login_url='/')
def DELETE_PROF(request,admin):
    prof = CustumUser.objects.get(id=admin)
    prof.delete()
    messages.success(request, 'suppression avec succès!')

    return redirect('view_prof')

@login_required(login_url='/')
def ADD_MATIERE(request):
    groupe = Groupe.objects.all()
    prof = Professeur.objects.all()
    if request.method == "POST":
        matiere_name=request.POST.get('matiere_name')
        groupe_id = request.POST.get('groupe_id')
        prof_id = request.POST.get('prof_id')

        groupe=Groupe.objects.get(id=groupe_id)
        prof=Professeur.objects.get(id= prof_id)
        matiere=Matiere(
            nom=matiere_name,
            groupe=groupe,
            professeur=prof ,
        )
        matiere.save()
        messages.success(request,"Matiére a été ajouté avec succès !")
        return redirect('ajouter_matiere')
    context = {
        'groupe':groupe,
        'prof': prof,
    }
    return render(request, 'Admin/ajouter_matiere.html',context)

@login_required(login_url='/')
def VIEW_MATIER(request):
    matiere=Matiere.objects.all()
    context = {
        'matiere': matiere,
    }
    return  render(request,'Admin/voir_matiere.html',context)

@login_required(login_url='/')
def EDIT_MATIERE(request,id):
      matiere=Matiere.objects.get(id =id)
      groupe = Groupe.objects.all()
      prof = Professeur.objects.all()
      context = {
          'matiere': matiere,
          'groupe' :groupe,
          'prof' : prof
      }
      return render(request, 'Admin/edit_matiere.html',context)


@login_required(login_url='/')
def UPDATE_MATIERE(request):
    if request.method == "POST":
        matiere_id=request.POST.get('matiere_id')
        matiere_name = request.POST.get('matiere_name')
        groupe_id=request.POST.get('groupe_id')
        prof_id=request.POST.get('prof_id')
        groupe=Groupe.objects.get(id = groupe_id)
        prof = Professeur.objects.get(id=prof_id)
        matiere = Matiere(
               id = matiere_id,
               nom=matiere_name,
               groupe=groupe,
               professeur=prof,
        )
        matiere.save()
        messages.success(request,"Matiére a été modifié avec succès  !")
        return redirect("view_matiere")

def DELETE_MATIERE(request,id):
    matiere=Matiere.objects.filter(id = id)
    matiere.delete()
    messages.success(request, "Matiére a été supprimé avec succès !")
    return redirect("view_matiere")

def ADD_SESSION(request):
    if request.method == "POST":
        session_year_start=request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session=Anne_de_session(
            debut_session= session_year_start,
            fin_session=session_year_end,
        )
        session.save()
        messages.success(request, "Session a été ajouté avec succès !")
        return redirect('add_session')
    return render(request,'Admin/ajouter_session.html')

def VIEW_SESSION(request):
    session=Anne_de_session.objects.all()

    context = {
        'session' : session,
    }
    return render(request, 'Admin/voir_session.html',context)


def EDIT_SESSION(request,id):
    session = Anne_de_session.objects.filter(id = id)
    context ={
        'session':session,
    }
    return render(request,'Admin/edit_session.html',context)


@login_required(login_url='/')
def UPDATE_SESSION(request):
    if request.method == "POST":
        session_id=request.POST.get('session_id')
        session_year_start = request.POST.get('session_year_start')
        session_year_end=request.POST.get('session_year_end')

        session =  Anne_de_session(
            id =  session_id,
            debut_session=session_year_start,
            fin_session=session_year_end,

        )
        session.save()
        messages.success(request,"la Session est mise à jour avec succès !")
        return redirect("view_session")


def DELETE_SESSION(request,id):
    session=Anne_de_session.objects.get(id = id)
    session.delete()
    messages.success(request, "la Session est supprimé avec succès !")
    return redirect("view_session")

def PROF_SEND_NOTIFICATION(request):
    prof=Professeur.objects.all()
    see_notification=Prof_Notification.objects.all().order_by('-id')[0:5]
    context={
        'prof':prof,
        'see_notification':see_notification,
    }
    return render(request,'Admin/prof_notification.html',context)

def SAVE_PROF_NOTIFICATION(request):
    if request.method=="POST":
        prof_id=request.POST.get('prof_id')
        message= request.POST.get('message')

        prof=Professeur.objects.get(admin = prof_id)
        notification=Prof_Notification(
            prof_id=prof,
            message=message,
        )
        notification.save()
        messages.success(request, "La notification a été envoyé avec succés !")

        return redirect('prof_send_notification')

def PROF_Leave_view(request):
    prof_conge=Professeur_conge.objects.all()
    context ={
        'prof_conge':prof_conge,
    }
    return render(request,"Admin/prof_conge.html",context)

def PROF_APPROVE_LEAVE(request,id):
    conge=Professeur_conge.objects.get(id= id)
    conge.status=1
    conge.save()
    return redirect('prof_leave_view')

def PROF_DISAPPROVE_LEAVE(request,id):
    conge = Professeur_conge.objects.get(id=id)
    conge.status = 2
    conge.save()
    return redirect('prof_leave_view')

def PROF_MESSAGE(request):
    feedback = Prof_message.objects.all()
    feedback_history =Prof_message.objects.all().order_by('-id')[0:5]
    context = {
        'feedback': feedback,
        'feedback_history': feedback_history
    }
    return render(request,'Admin/prof_message.html',context)

def PROF_MESSAGE_SAVE(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply= request.POST.get('feedback_reply')

        feedback = Prof_message.objects.get(id=feedback_id)
        feedback. reponse_message=feedback_reply
        feedback.status=1
        feedback.save()
    return redirect('prof_feedback_reply')

def STUDENT_MESSAGE(request):
    feedback = Etudiant_message.objects.all()
    feedback_history=Etudiant_message.objects.all().order_by('-id')[0:5]
    context = {
        'feedback':feedback,
        'feedback_history':feedback_history
    }
    return render(request,"Admin/etudiant_message.html",context)

def REPLY_STUDENT_MESSAGE(request):
    if request.method == "POST":
        feedback_id=request.POST.get('feedback_id')
        feedback_reply= request.POST.get('feedback_reply')

        feedback = Etudiant_message.objects.get(id=feedback_id)
        feedback.message_reponse = feedback_reply
        feedback.status=1
        feedback.save()
        return redirect('get_student_feedback')


def STUDENT_SEND_NOTIFICATION(request):
    etudiant=Etudiant.objects.all()
    notification=Etudiant_Notification.objects.all()
    context={
        'student':etudiant,
        'notification':notification
    }
    return render(request,'Admin/etudiant_notification.html',context)

def STUDENT_SAVE_NOTIFICATION(request):
    if request.method == "POST":
        message=request.POST.get('message')
        student_id=request.POST.get('student_id')
        student=Etudiant.objects.get(admin=student_id)
        stud_notification=Etudiant_Notification(
            etudiant_id=student,
            message=message,
        )
        stud_notification.save()
        messages.success(request, "La notification a été envoyé avec succés !")

        return redirect('student_send_notification')

def VIEW_ABSCANCE(request):

    matiere = Matiere.objects.all()
    session_year = Anne_de_session.objects.all()

    action = request.GET.get('action')
    get_matiere = None
    get_session_year = None
    abscence_date = None
    abscence_raport  = None

    if action is not None:
        if request.method == "POST":
            matiere_id = request.POST.get('matiere_id')
            session_year_id = request.POST.get('session_year_id')
            abscence_date = request.POST.get('abscence_date')

            get_matiere = Matiere.objects.get(id=matiere_id)
            get_session_year = Anne_de_session.objects.get(id=session_year_id)

            abscence = Abscence.objects.filter(
                matiere_id=get_matiere,
               abscence_data=abscence_date
            )

            for i in abscence:
                abscence_id = i.id

                abscence_raport =Abscence_Raport.objects.filter(
                    abscence_id=abscence_id,

                )

    context = {
        'matiere': matiere,
        'session_year': session_year,
        'action': action,
        'get_matiere': get_matiere,
        'get_session_year': get_session_year,
        'abscence_date': abscence_date,
        'abscence_raport': abscence_raport
    }
    return render(request,'Admin/voir_abscence',context)