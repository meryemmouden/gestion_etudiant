from django.shortcuts import render,redirect

from app.models import Etudiant, Etudiant_Notification, Etudiant_message, Matiere, \
    Abscence_Raport, EtudiantResultat


def HOME(request):
    return render(request,'Etudiant/home.html')



def STUDENT_NOTIFICATION(request):
    student = Etudiant.objects.filter(admin =request.user.id)
    for i in student:
        student_id= i.id
        notifications=Etudiant_Notification.objects.filter(etudiant_id= student_id)
        print(notifications)
        context = {
            'notifications':notifications
        }
    return render(request,'Etudiant/notification.html',context)

def STUDENT_NOTIFICATION_MARK_AS_DONE(request,status):
    notification=Etudiant_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('student_notification')

def STUDENT_FEEDBACK(request):
    student_id=Etudiant.objects.get(admin=request.user.id)
    feedback_history=Etudiant_message.objects.filter(etudiant_id=student_id)
    context ={
        "feedback_history":feedback_history
    }
    return render(request, 'Etudiant/message.html',context)

def STUDENT_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        student = Etudiant.objects.get(admin=request.user.id)
        feedback = Etudiant_message(
            etudiant_id=student,
            message=feedback,
            message_reponse="",
        )
        feedback.save()
    return redirect('student_feedback')


def STUDENT_VIEW_ABSCENCE(request):
    student=Etudiant.objects.get(admin=request.user.id)
    matiers = Matiere.objects.filter(groupe=student.groupe_id)
    action = request.GET.get('action')

    get_matiere=None
    abscence_rapport=None
    if action is not None:
        if request.method == "POST":
            matiere_id=request.POST.get('matiere_id')
            get_matiere=Matiere.objects.get(id=matiere_id)
            abscence_rapport = Abscence_Raport.objects.filter(
                etudiant_id=student,
                abscence_id__matiere_id=matiere_id
            )
    context={
        'matiers':matiers,
        'action': action,
        'get_matiere': get_matiere,
        'abscence_rapport': abscence_rapport
    }
    return render(request,'Etudiant/voir_abscence.html',context)


def VIEW_RESULT(request):

    student=Etudiant.objects.get(admin=request.user.id)
    result=EtudiantResultat.objects.filter(etudiant_id=student)

    context={
        'result':result,

    }
    return render(request,'Etudiant/voir_resultat.html',context)