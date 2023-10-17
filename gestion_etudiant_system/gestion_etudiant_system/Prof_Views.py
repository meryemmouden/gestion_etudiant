from django.shortcuts import render,redirect

from app.models import Professeur, Prof_Notification, Professeur_conge, Prof_message, \
    Anne_de_session, Matiere, Etudiant, Abscence, Abscence_Raport, EtudiantResultat
from django.contrib import messages

def Home(request):
    return render(request,'Prof/home.html')

def NOTIFICATIONS(request):
    professeur=Professeur.objects.filter(admin =request.user.id)
    for i in professeur:
        prof_id= i.id
        notification=Prof_Notification.objects.filter(prof_id = prof_id)
        context={
            'notification':notification
        }
    return render(request,'Prof/notification.html',context)

def PROF_NOTIFICATION_MARK_AS_DONE(request,status):
    notification=Prof_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('notification')

def PROF_APPLY_LEAVE(request):
    prof=Professeur.objects.filter(admin=request.user.id)
    for i in prof:
        prof_id=i.id
        prof_leave_history=Professeur_conge.objects.filter(professeur_id = prof_id)
        context={
        'prof_leave_history':prof_leave_history}
    return render(request,'Prof/conge.html',context)

def PROF_APPLY_LEAVE_SAVE(request):
    if request.method == "POST" :
        leave_date=request.POST.get('leave_date')
        leave_message=request.POST.get('leave_message')
        prof=Professeur.objects.get(admin=request.user.id)

        leave=Professeur_conge(
            professeur_id=prof,
            data=leave_date,
            message=leave_message,
        )
        leave.save()
        messages.success(request,"Abscence envoyé avec succès")
        return redirect('prof_apply_leave')

def PROF_FEEDBACK(request):
    prof = Professeur.objects.get(admin=request.user.id)
    feedback_history=Prof_message.objects.filter(prof_id=prof)
    context={
        'feedback_history':feedback_history,
    }

    return render(request,'Prof/message.html',context)


def PROF_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback=request.POST.get('feedback')
        prof=Professeur.objects.get(admin=request.user.id)
        feedback=Prof_message(
            prof_id=prof,
            message=feedback,
            reponse_message="",
        )
        feedback.save()
    return redirect('prof_feedback')

def PROF_TAKE_ABSCENCE(request):
    prof_id=Professeur.objects.get(admin=request.user.id)
    matiere=Matiere.objects.filter(professeur=prof_id)
    session_year=Anne_de_session.objects.all()
    action=request.GET.get('action')
    students=None
    get_matiere =None
    get_session_year=None
    if action is not None:
        if request.method == "POST":
           matiere_id=request.POST.get('matiere_id')
           session_year_id=request.POST.get('session_year_id')
           get_matiere = Matiere.objects.get(id=matiere_id)
           get_session_year = Anne_de_session.objects.get(id=session_year_id)

           matiere=Matiere.objects.filter(id=matiere_id)
           for i in matiere:
              student_id=i.groupe.id
              students =Etudiant.objects.filter( groupe_id =student_id)

    context={
        'matiere':matiere,
        'session_year':session_year,
        'get_matiere':get_matiere,
        'get_session_year': get_session_year,
        'action':action,
        'students':students

    }
    return render(request,'Prof/prend_abscence.html',context)

def PROF_SAVE_ABSCENCE(request):
    if request.method == "POST":
        matiere_id=request.POST.get('matiere_id')
        session_year_id = request.POST.get('session_year_id')
        abscence_date = request.POST.get('abscence_date')
        student_id=request.POST.getlist('student_id')

        get_matiere=Matiere.objects.get(id=matiere_id)
        get_session_year=Anne_de_session.objects.get(id=session_year_id)

        abscence =Abscence(
            matiere_id=get_matiere,
            abscence_data=abscence_date,
            anne_session_id=get_session_year
        )
        abscence.save()
        for i in student_id :
            stud_id=i
            int_stud=int(stud_id)

            p_students=Etudiant.objects.get(id=int_stud)
            abscence_Raport=Abscence_Raport(
                etudiant_id=p_students,
                abscence_id=abscence,
            )
            abscence_Raport.save()
        return redirect('prof_take_abscence')

def PROF_VIEW_ABSCENCE(request):

    prof_id=Professeur.objects.get(admin=request.user.id)
    matiere=Matiere.objects.filter( professeur=prof_id)
    session_year = Anne_de_session.objects.all()

    action=request.GET.get('action')
    get_matiere=None
    get_session_year=None
    abscence_date=None
    abscence_rapport=None

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

                abscence_rapport = Abscence_Raport.objects.filter(
                    abscence_id=abscence_id,

                )


    context ={
        'matiere':matiere,
        'session_year':session_year,
        'action':action,
         'get_matiere':get_matiere,
        'get_session_year':get_session_year,
        'abscence_date' :abscence_date,
        'abscence_report':abscence_rapport
    }
    return render(request,'Prof/voir_abscence.html',context)

def PROF_ADD_RESULT(request):
    prof = Professeur.objects.get(admin = request.user.id)

    matiere = Matiere.objects.filter(professeur= prof)
    session_year = Anne_de_session.objects.all()
    action = request.GET.get('action')
    get_matiere = None
    get_session = None
    students = None
    if action is not None:
        if request.method == "POST":
           matiere_id = request.POST.get('matiere_id')
           session_year_id = request.POST.get('session_year_id')

           get_matiere = Matiere.objects.get(id = matiere_id)
           get_session = Anne_de_session.objects.get(id = session_year_id)

           matiere = Matiere.objects.filter(id = matiere_id)
           for i in matiere:
               student_id = i.groupe.id
               students = Etudiant.objects.filter(groupe_id = student_id)


    context = {
        'matiers':matiere,
        'session_year':session_year,
        'action':action,
        'get_matiere':get_matiere,
        'get_session':get_session,
        'students':students,
    }

    return render(request,'Prof/ajouter_resultat.html',context)


def PROF_SAVE_RESULT(request):
    if request.method == "POST":
        matiere_id = request.POST.get('matiere_id')
        session_year_id = request.POST.get('session_year_id')
        student_id = request.POST.get('student_id')
        controle = request.POST.get('controle')
        exam = request.POST.get('exam')

        get_student = Etudiant.objects.get(admin = student_id)
        get_matiere = Matiere.objects.get(id=matiere_id)

        check_exist = EtudiantResultat.objects.filter(matiere_id=get_matiere, etudiant_id=get_student).exists()
        if check_exist:
            result =EtudiantResultat.objects.get(matiere_id=get_matiere, etudiant_id=get_student)
            result.controle_note = controle
            result.exam_note = exam
            result.save()
            messages.success(request, "Résultat modifié avec succès")
            return redirect('prof_add_result')
        else:
            result = EtudiantResultat(etudiant_id=get_student, matiere_id=get_matiere,exam_note=exam, controle_note=controle)
            result.save()
            messages.success(request, "Résultat ajouté avec succès")
            return redirect('prof_add_result')