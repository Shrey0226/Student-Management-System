from django.shortcuts import render, redirect
from management.models import Faculty, Faculty_notification, Faculty_leave, Faculty_feedback, Subject, Attendence, Attendence_report, Session
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def HOME(request):
    return render(request, 'faculty/home.html')


@login_required(login_url='/')
def NOTIFICATIONS(request):
    faculty = Faculty.objects.filter(admin=request.user.id)
    for i in faculty:
        faculty_id = i.id
        notifications = Faculty_notification.objects.filter(
            faculty_id=faculty_id)
        context = {
            'notifications': notifications
        }
    return render(request, 'faculty/notification.html', context)


@login_required(login_url='/')
def READ_NOTIFICATIONS(request, status):
    notification = Faculty_notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('notifications')


@login_required(login_url='/')
def APPLY_LEAVE(request):
    faculty_leave = Faculty_leave.objects.all()
    context = {
        'faculty_leave': faculty_leave
    }
    if request.method == "POST":
        date = request.POST.get('date')
        message = request.POST.get('message')
        faculty_id = Faculty.objects.get(admin=request.user.id)
        leave = Faculty_leave(
            date=date,
            message=message,
            faculty_id=faculty_id,
        )
        leave.save()
        messages.success(request, "Applied for leave Successfully!")
        return redirect('faculty_apply_leave')
    return render(request, "faculty/apply_leave.html", context)


@login_required(login_url='/')
def SEND_FEEDBACK(request):
    faculty_feedback = Faculty_feedback.objects.all()
    context = {
        'faculty_feedback': faculty_feedback,
    }
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        faculty = Faculty.objects.get(admin=request.user.id)
        send_feedback = Faculty_feedback(
            faculty_id=faculty,
            feedback=feedback,
            feedback_reply="",
        )
        send_feedback.save()
        messages.success(request, "Feedback sent Successfully!")
        return redirect('faculty_send_feedback')
    return render(request, 'faculty/send_feedback.html', context)


@login_required(login_url='/')
def FACULTY_MARK_ATTENDENCE(request):
    faculty = Faculty.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(faculty=faculty)
    session_year_id = Session.objects.all()
    action = request.GET.get('action')

    get_subject = None
    get_session = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_id = request.POST.get('session_id')
            print(subject_id, session_id)
            get_subject = Subject.objects.get(id=subject_id)
            get_session = Session.objects.get(id=session_id)

    context = {
        'subject': subject,
        'session_year_id': session_year_id,
        'get_subject': get_subject,
        'get_session': get_session,
    }
    return render(request, 'faculty/mark_attendence.html', context)
