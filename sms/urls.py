"""sms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from .import faculty_views, views, hod_views, student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),

    # login panel
    path('', views.LOGIN, name='login'),
    path('dologin', views.dologin, name='dologin'),
    path('dologout', views.dologout, name='logout'),

    # profile panel
    path('Profile/', views.PROFILE, name='profile'),
    path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),

    # hod panel url
    path('Hod/home', hod_views.HOME, name='hod_home'),

    path('Hod/Student/Add', hod_views.ADD_STUDENT, name="add_student"),
    path('Hod/Student/View', hod_views.VIEW_STUDENT, name="view_student"),
    path('Hod/Student/Edit/<str:id>', hod_views.EDIT_STUDENT, name="edit_student"),
    path('Hod/Student/Update', hod_views.UPDATE_STUDENT, name="update_student"),
    path('Hod/student/Delete/<str:admin>',
         hod_views.DELETE_STUDENT, name="delete_student"),

    path('Hod/Course/Add', hod_views.ADD_COURSE, name="add_course"),
    path('Hod/Course/View', hod_views.VIEW_COURSE, name="view_course"),
    path('Hod/Course/Edit/<str:id>', hod_views.EDIT_COURSE, name="edit_course"),
    path('Hod/course/update', hod_views.UPDATE_COURSE, name="update_course"),
    path('Hod/Course/Delete/<str:id>',
         hod_views.DELETE_COURSE, name="delete_course"),

    path('Hod/Faculty/Add', hod_views.ADD_FACULTY, name="add_faculty"),
    path('Hod/Faculty/View', hod_views.VIEW_FACULTY, name="view_faculty"),
    path('Hod/Faculty/Edit/<str:id>', hod_views.EDIT_FACULTY, name="edit_faculty"),
    path('Hod/Faculty/Update', hod_views.UPDATE_FACULTY, name="update_faculty"),
    path('Hod/Faculty/Delete/<str:admin>',
         hod_views.DELETE_FACULTY, name="delete_faculty"),

    path('Hod/Subject/Add', hod_views.ADD_SUBJECT, name="add_subject"),
    path('Hod/Subject/View', hod_views.VIEW_SUBJECT, name="view_subject"),
    path('Hod/Subject/Edit/<str:id>', hod_views.EDIT_SUBJECT, name="edit_subject"),
    path('Hod/Subject/Update', hod_views.UPDATE_SUBJECT, name="update_subject"),
    path('Hod/Subject/Delete/<str:id>',
         hod_views.DELETE_SUBJECT, name="delete_subject"),

    path('Hod/Session/Add', hod_views.ADD_SESSION, name="add_session"),
    path('Hod/Session/View', hod_views.VIEW_SESSION, name="view_session"),
    path('Hod/Session/Edit/<str:id>', hod_views.EDIT_SESSION, name="edit_session"),
    path('Hod/Session/Update', hod_views.UPDATE_SESSION, name="update_session"),

    path('Hod/Faculty/Send/Notification',
         hod_views.FACULTY_SEND_NOTIFICATION, name="faculty_send_notification"),
    path('Hod/Faculty/Save/Notification',
         hod_views.FACULTY_SAVE_NOTIFICATION, name="faculty_save_notification"),

    path('Hod/Faculty/Leave', hod_views.FACULTY_LEAVE, name="faculty_leave"),
    path('Hod/Faculty/Leave/Accept/<str:status>',
         hod_views.ACCEPT_FACULTY_LEAVE, name="accept_faculty_leave"),
    path('Hod/Faculty/Leave/Reject/<str:status>',
         hod_views.REJECT_FACULTY_LEAVE, name="reject_faculty_leave"),

    path('Hod/Faculty/Read/Feedback', hod_views.READ_FACULTY_FEEDBACK,
         name="read_faculty_feedback"),
    path('Hod/Faculty/Reply/Feedback', hod_views.REPLY_FACULTY_FEEDBACK,
         name="reply_faculty_feedback"),

    path('Hod/Student/Send/Notification',
         hod_views.STUDENT_SEND_NOTIFICATION, name="student_send_notification"),
    path('Hod/Student/Save/Notification',
         hod_views.STUDENT_SAVE_NOTIFICATION, name="student_save_notification"),
    path('Hod/Student/Leave', hod_views.HOD_STUDENT_LEAVE,
         name="hod_student_leave"),
    path('Hod/Student/Leave/Accept/<str:status>',
         hod_views.ACCEPT_STUDENT_LEAVE, name="accept_student_leave"),
    path('Hod/Student/Leave/Reject/<str:status>',
         hod_views.REJECT_STUDENT_LEAVE, name="reject_student_leave"),
    path('Hod/Student/Read/Feedback', hod_views.READ_STUDENT_FEEDBACK,
         name="read_student_feedback"),
    path('Hod/Student/Reply/Feedback', hod_views.REPLY_STUDENT_FEEDBACK,
         name="reply_student_feedback"),

    # faculty urls

    path('Faculty/home', faculty_views.HOME, name="faculty_home"),
    path('Faculty/Notifications', faculty_views.NOTIFICATIONS, name="notifications"),
    path('Faculty/Read/Notifications/<str:status>',
         faculty_views.READ_NOTIFICATIONS, name="read_notifications"),
    path('Faculty/Leave/Apply', faculty_views.APPLY_LEAVE,
         name="faculty_apply_leave"),
    path('Faculty/Send/Feedback', faculty_views.SEND_FEEDBACK,
         name="faculty_send_feedback"),
    path('Faculty/Mark/Attendence', faculty_views.FACULTY_MARK_ATTENDENCE,
         name="faculty_mark_attendence"),

    # student urls
    path('Student/home', student_views.HOME, name="student_home"),
    path('Student/Notification', student_views.STUDENT_NOTIFICATION,
         name="student_get_notification"),
    path('Student/Read/Notification/<str:status>', student_views.STUDENT_READ_NOTIFICATION,
         name="student_read_notifications"),
    path('Student/Leave', student_views.STUDENT_APPLY_LEAVE, name="student_leave"),
    path('Student/Send/Feedback', student_views.STUDENT_SEND_FEEDBACK,
         name="student_send_feedback"),
    path('Student/Save/Feedback', student_views.STUDENT_SAVE_FEEDBACK,
         name="student_save_feedback"),
    path('Student/View/Subjects', student_views.STUDENT_VIEW_SUBJECT,
         name="student_view_subject")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
