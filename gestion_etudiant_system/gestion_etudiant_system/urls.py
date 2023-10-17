
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import Admin_Views,Prof_Views,Etudiant_Views,views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),

    #login path
    path('', views.CONNEXION, name='login'),
    path('doLogin', views.FAIRE_CONNEXION, name='doLogin'),
    path('doLogout', views.FAIRE_DECONNEXION, name='Logout'),
    # profile updates
    path('Profile', views.PROFILE, name='profile'),
    path('Profile/update', views.MODIFIE_PROFIL, name='profile_update'),
#this is hod panel  url
                  path('Admin/Home', Admin_Views.HOME, name='admin_home'),
                  path('Admin/etudiant/ajouter', Admin_Views.ADD_STUDENT, name='ajouter_etudiant'),
                  path('Admin/groupe/ajouter',Admin_Views.ADD_GROUPE,name='ajouter_groupe'),
                  path('Admin/matiere/ajouter', Admin_Views.ADD_MATIERE, name='ajouter_matiere'),
                  path('Admin/prof/ajouter', Admin_Views.ADD_PROF, name='add_prof'),
                  path('Admin/session/ajouter', Admin_Views.ADD_SESSION, name='add_session'),

                  path('Admin/etudiant/edit/<str:id>', Admin_Views.EDIT_STUDENT, name='edit_student'),
                  path('Admin/professeur/edit/<str:id>', Admin_Views.EDIT_PROF, name='edit_prof'),
                  path('Admin/groupe/edit/<str:id>',Admin_Views.EDIT_GROUPE, name='edit_groupe'),
                  path('Admin/matiere/edit/<str:id>',Admin_Views.EDIT_MATIERE, name='edit_matiere'),
                  path('Admin/session/edit/<str:id>',Admin_Views.EDIT_SESSION, name='edit_session'),

                  path('Admin/Student/Update', Admin_Views.UPDATE_STUDENT, name='update_student'),
                  path('Admin/Student/Delete/<str:admin>', Admin_Views.DELETE_STUDENT, name='delete_student'),
                  path('Admin/Student/View',Admin_Views.VIEW_STUDENT,name='voir_student'),

                  path('Admin/prof/View', Admin_Views.VIEW_PROF, name='view_prof'),
                  path('Admin/prof/Update', Admin_Views.UPDATE_PROF, name='update_prof'),
                  path('Admin/prof/Delete/<str:admin>', Admin_Views.DELETE_PROF, name='delete_prof'),


                  path('Admin/group/View', Admin_Views.VIEW_GROUPE, name='view_groupe'),
                  path('Admin/group/Update',Admin_Views.UPDATE_GROUPE,name='update_groupe'),
                  path('Admin/group/Delete/<str:id>',Admin_Views.DELETE_GROUPE,name='delete_groupe'),

                  path('Admin/matiere/View',  Admin_Views.VIEW_MATIER, name='view_matiere'),
                  path('Admin/matiere/Update',  Admin_Views.UPDATE_MATIERE, name='update_matiere'),
                  path('Admin/matiere/Delete/<str:id>',  Admin_Views.DELETE_MATIERE, name='delete_matiere'),

                  path('Admin/session/View', Admin_Views.VIEW_SESSION, name='view_session'),
                  path('Admin/session/Update',Admin_Views.UPDATE_SESSION, name='update_session'),
                  path('Admin/session/Delete/<str:id>', Admin_Views.DELETE_SESSION, name='delete_session'),

                  path('Admin/View/Abscance', Admin_Views.VIEW_ABSCANCE, name='view_abscence'),

                  path('Admin/Student/feedback', Admin_Views.STUDENT_MESSAGE, name='get_student_feedback'),
                  path('Admin/Student/feedback/reply/save', Admin_Views.REPLY_STUDENT_MESSAGE, name='reply_student_feedback'),
                  path('Admin/prof/feedback', Admin_Views.PROF_MESSAGE, name='prof_feedback_reply'),
                  path('Admin/prof/feedback/save', Admin_Views.PROF_MESSAGE_SAVE, name='prof_feedback_reply_save'),

                  path('Admin/prof/disapprove_Leave/<str:id>', Admin_Views.PROF_DISAPPROVE_LEAVE,name='prof_disapprove_leave'),
                  path('Admin/prof/Leave_view', Admin_Views.PROF_Leave_view, name='prof_leave_view'),
                  path('Admin/prof/approve_Leave/<str:id>', Admin_Views.PROF_APPROVE_LEAVE, name='prof_approve_leave'),

                  path('Admin/prof/Save_Notification', Admin_Views.SAVE_PROF_NOTIFICATION, name='save_prof_notification'),
                  path('Admin/prof/Send_Notification', Admin_Views.PROF_SEND_NOTIFICATION, name='prof_send_notification'),
                   path('Admin/Student/send_notification',Admin_Views.STUDENT_SEND_NOTIFICATION, name='student_send_notification'),
                  path('Admin/Student/save_notification', Admin_Views.STUDENT_SAVE_NOTIFICATION,name='student_save_notification'),

                  # this is staff
                  path('Prof/Home', Prof_Views.Home, name='prof_home'),

                  path('Prof/Notification', Prof_Views.NOTIFICATIONS, name='notification'),
                  path('Prof/mark_as_done/<str:status>', Prof_Views.PROF_NOTIFICATION_MARK_AS_DONE,name='prof_notification_mark_as_done'),

                  path('Prof/Apply_leave', Prof_Views.PROF_APPLY_LEAVE, name='prof_apply_leave'),
                  path('Prof/Apply_leave_save', Prof_Views.PROF_APPLY_LEAVE_SAVE, name='prof_apply_leave_save'),

                  path('prof/message', Prof_Views.PROF_FEEDBACK, name='prof_feedback'),
                  path('prof/message/Save', Prof_Views.PROF_FEEDBACK_SAVE, name='prof_feedback_save'),

                  path('prof/prend_abscence', Prof_Views.PROF_TAKE_ABSCENCE, name='prof_take_abscence'),
                  path('prof/Save_abscence', Prof_Views.PROF_SAVE_ABSCENCE, name='prof_save_abscence'),

                  path('prof/Voir_abscence', Prof_Views.PROF_VIEW_ABSCENCE, name='prof_voir_abscence'),
                  path('prof/Add/Result', Prof_Views.PROF_ADD_RESULT, name='prof_add_result'),
                  path('prof/Save/Result', Prof_Views.PROF_SAVE_RESULT, name='prof_save_result'),
                  # Student Urls
                  path('Student/Home', Etudiant_Views.HOME, name='student_home'),

                  path('Student/Notifications', Etudiant_Views.STUDENT_NOTIFICATION, name='student_notification'),
                  path('Student/mark_as_done/<str:status>', Etudiant_Views.STUDENT_NOTIFICATION_MARK_AS_DONE, name='student_notification_mark_as_done'),

                  path('Student/Feedback', Etudiant_Views.STUDENT_FEEDBACK, name='student_feedback'),
                  path('Student/Feedback/Save', Etudiant_Views.STUDENT_FEEDBACK_SAVE, name='student_feedback_save'),


                  path('Student/View_Abscence', Etudiant_Views.STUDENT_VIEW_ABSCENCE,name='student_view_abscence'),
                  path('Student/View_Result',Etudiant_Views.VIEW_RESULT, name='view_result'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
