from django.shortcuts import render, redirect
from management.models import student, Student_notification, Student_leave, Student_feedback, Subject
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def HOME(request):
    return render(request, "student/home.html")


@login_required(login_url='/')
def STUDENT_NOTIFICATION(request):
    Student = student.objects.filter(admin=request.user.id)
    for i in Student:
        student_id = i.id
        notifications = Student_notification.objects.filter(
            student_id=student_id)
        context = {
            'notifications': notifications
        }
    return render(request, 'student/notification.html', context)


@login_required(login_url='/')
def STUDENT_READ_NOTIFICATION(request, status):
    notification = Student_notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('student_get_notification')


@login_required(login_url='/')
def STUDENT_APPLY_LEAVE(request):
    if request.method == "POST":
        student_id = student.objects.get(admin=request.user.id)
        date = request.POST.get('date')
        message = request.POST.get('message')
        leave = Student_leave(
            student_id=student_id,
            date=date,
            message=message,
        )
        leave.save()
        messages.success(request, "Leave applied successfully!")
        return redirect('student_leave')

    student_leave = Student_leave.objects.all()
    context = {
        'student_leave': student_leave,
    }
    return render(request, 'student/leave.html', context)


@login_required(login_url='/')
def STUDENT_SEND_FEEDBACK(request):
    student_feedback = Student_feedback.objects.all()
    context = {
        'student_feedback': student_feedback,
    }
    return render(request, 'student/feedback.html', context)


@login_required(login_url='/')
def STUDENT_SAVE_FEEDBACK(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        Student = student.objects.get(admin=request.user.id)
        send_feedback = Student_feedback(
            student_id=Student,
            feedback=feedback,
            feedback_reply="",
        )
        send_feedback.save()
        messages.success(request, "Feedback sent Successfully!")
    return redirect('student_send_feedback')


@login_required(login_url='/')
def STUDENT_VIEW_SUBJECT(request):
    Student = student.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(course=Student.course_id)
    context = {
        'subject': subject
    }
    return render(request, 'student/mycourses.html', context)
