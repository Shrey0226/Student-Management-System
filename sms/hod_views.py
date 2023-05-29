from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from management.models import Course, Session, CustomUser, student, Faculty, Subject, Faculty_notification, Faculty_leave, Faculty_feedback, Student_notification, Student_leave, Student_feedback
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    student_count = student.objects.all().count()
    faculty_count = Faculty.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()
    student_gender_male = student.objects.filter(gender='male').count()
    student_gender_female = student.objects.filter(gender='female').count()
    student_gender_others = student.objects.filter(gender='others').count()
    faculty_gender_male = Faculty.objects.filter(gender='male').count()
    faculty_gender_female = Faculty.objects.filter(gender='female').count()
    faculty_gender_others = Faculty.objects.filter(gender='others').count()

    context = {
        'student_count': student_count,
        'faculty_count': faculty_count,
        'course_count': course_count,
        'subject_count': subject_count,
        'student_gender_male': student_gender_male,
        'student_gender_female': student_gender_female,
        'student_gender_others': student_gender_others,
        'faculty_gender_others': faculty_gender_others,
        'faculty_gender_female': faculty_gender_female,
        'faculty_gender_male': faculty_gender_male,
    }
    return render(request, 'hod/home.html', context)


@login_required(login_url='/')
def ADD_STUDENT(request):
    course = Course.objects.all()
    session = Session.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        father_name = request.POST.get('father_name')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already taken')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is already taken')
            return redirect('add_student')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                profile_pic=profile_pic,
                username=username,
                user_type=3,
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)
            session = Session.objects.get(id=session_year_id)

            Student = student(
                admin=user,
                address=address,
                father_name=father_name,
                phone_no=phone_no,
                gender=gender,
                course_id=course,
                session_year_id=session,
            )
            Student.save()
            messages.success(request, 'Added student successfully!')
            return redirect('add_student')

    context = {
        'course': course,
        'session': session,
    }
    return render(request, 'hod/add_student.html', context)


@login_required(login_url='/')
def VIEW_STUDENT(request):
    Student = student.objects.all()

    context = {
        'Student': Student,
    }
    return render(request, 'hod/view_student.html', context)


@login_required(login_url='/')
def EDIT_STUDENT(request, id):
    Student = student.objects.filter(id=id)
    course = Course.objects.all()
    session = Session.objects.all()
    context = {
        'Student': Student,
        'course': course,
        'session': session,
    }
    return render(request, 'hod/edit_student.html', context)


@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        father_name = request.POST.get('father_name')
        phone_no = request.POST.get('phone_no')
        password = request.POST.get('password')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        user = CustomUser.objects.get(id=student_id)
        user.first_name = first_name
        user.last_name = last_name
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        if password != None and password != "":
            user.set_password(password)
        user.save()

        course = Course.objects.get(id=course_id)
        session = Session.objects.get(id=session_year_id)
        Student = student.objects.get(admin=student_id)
        Student.gender = gender
        Student.address = address
        Student.father_name = father_name
        Student.phone_no = phone_no
        Student.course_id = course
        Student.session_year_id = session
        Student.save()

        messages.success(request, 'Updated the details Successfully')
        return redirect('view_student')

    return render(request, 'hod/edit_student.html')


@login_required(login_url='/')
def DELETE_STUDENT(request, admin):
    Student = CustomUser.objects.get(id=admin)
    Student.delete()

    messages.success(request, 'Student details deleted successfully !')
    return redirect('view_student')


@login_required(login_url='/')
def ADD_COURSE(request):
    if request.method == "POST":
        course_name = request.POST.get("course_name")
        course = Course(
            name=course_name,
        )
        course.save()
        messages.success(request, 'Course added Successfully!')
        return redirect('add_course')
    return render(request, 'hod/add_course.html')


@login_required(login_url='/')
def VIEW_COURSE(request):
    course = Course.objects.all()
    context = {
        'course': course,
    }
    return render(request, 'hod/view_course.html', context)


@login_required(login_url='/')
def EDIT_COURSE(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course': course,
    }
    return render(request, 'hod/edit_course.html', context)


@login_required(login_url='/')
def UPDATE_COURSE(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')
        course_id = request.POST.get('course_id')
        course = Course.objects.get(id=course_id)
        course.name = course_name
        course.save()
        messages.success(request, "Course updated Successfully!")
        return redirect('view_course')
    return render(request, 'hod/edit_course.html')


@login_required(login_url='/')
def DELETE_COURSE(request, id):
    course = Course.objects.get(id=id)
    course.delete()

    messages.success(request, "Course deleted Successfully!")
    return redirect('view_course')


@login_required(login_url='/')
def ADD_FACULTY(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        phone_no = request.POST.get('phone_no')
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already taken')
            return redirect('add_faculty')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is already taken')
            return redirect('add_faculty')
        else:
            user = CustomUser(
                profile_pic=profile_pic,
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                user_type=2,
            )
            user.set_password(password)
            user.save()

            faculty = Faculty(
                admin=user,
                gender=gender,
                address=address,
                phone_no=phone_no,
            )
            faculty.save()

            messages.success(request, "Faculty added successfully!")
            return redirect('add_faculty')

    return render(request, 'hod/add_faculty.html')


@login_required(login_url='/')
def VIEW_FACULTY(request):
    faculty = Faculty.objects.all()
    context = {
        'faculty': faculty,
    }
    return render(request, 'hod/view_faculty.html', context)


@login_required(login_url='/')
def EDIT_FACULTY(request, id):
    faculty = Faculty.objects.get(id=id)
    context = {
        'faculty': faculty,
    }
    return render(request, 'hod/edit_faculty.html', context)


@login_required(login_url='/')
def UPDATE_FACULTY(request):
    if request.method == "POST":
        faculty_id = request.POST.get('faculty_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        phone_no = request.POST.get('phone_no')

        user = CustomUser.objects.get(id=faculty_id)
        user.first_name = first_name
        user.last_name = last_name
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        if password != None and password != "":
            user.set_password(password)
        user.save()
        faculty = Faculty.objects.get(admin=user)
        faculty.gender = gender
        faculty.address = address
        faculty.phone_no = phone_no
        faculty.save()
        messages.success(request, "Faculty updated Successfully!")
        return redirect('view_faculty')

    return render(request, 'hod/edit_faculty.html')


@login_required(login_url='/')
def DELETE_FACULTY(request, admin):
    faculty = CustomUser.objects.get(id=admin)
    faculty.delete()
    messages.success(request, "Faculty deleted Successfully!")
    return redirect('view_faculty')


@login_required(login_url='/')
def ADD_SUBJECT(request):
    course = Course.objects.all()
    faculty = Faculty.objects.all()

    if request.method == "POST":
        name = request.POST.get('subject_name')
        course_id = request.POST.get("course_id")
        faculty_id = request.POST.get('faculty_id')

        course = Course.objects.get(id=course_id)
        faculty = Faculty.objects.get(id=faculty_id)

        subject = Subject(
            name=name,
            course=course,
            faculty=faculty,
        )
        subject.save()
        messages.success(request, "Subject added Successfully!")
        return redirect('add_subject')
        # print(name, course_id, faculty_id)
    context = {
        'course': course,
        'faculty': faculty,
    }
    return render(request, 'hod/add_subject.html', context)


@login_required(login_url='/')
def VIEW_SUBJECT(request):
    subject = Subject.objects.all()
    context = {
        'subject': subject,
    }
    return render(request, 'hod/view_subject.html', context)


@login_required(login_url='/')
def EDIT_SUBJECT(request, id):
    subject = Subject.objects.get(id=id)
    faculty = Faculty.objects.all()
    course = Course.objects.all()
    context = {
        'subject': subject,
        'faculty': faculty,
        'course': course,
    }
    return render(request, 'hod/edit_subject.html', context)


@login_required(login_url='/')
def UPDATE_SUBJECT(request):
    if request.method == "POST":
        id = request.POST.get('subject_id')
        name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        faculty_id = request.POST.get('faculty_id')

        course = Course.objects.get(id=course_id)
        faculty = Faculty.objects.get(id=faculty_id)
        subject = Subject.objects.get(id=id)

        subject.name = name
        subject.course = course
        subject.faculty = faculty
        subject.save()
        messages.success(request, "Subject updated successfully!")
        return redirect('view_subject')

    return render(request, 'hod/edit_subject.html')


@login_required(login_url='/')
def DELETE_SUBJECT(request, id):
    subject = Subject.objects.get(id=id)
    subject.delete()
    messages.success(request, "Subject deleted Successfully!")
    return redirect('view_subject')


@login_required(login_url='/')
def ADD_SESSION(request):
    if request.method == "POST":
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')
        session = Session(
            session_start=session_start,
            session_end=session_end,
        )
        session.save()
        messages.success(request, "Session generated successfully!")
        return redirect('add_session')
    return render(request, "hod/add_session.html")


@login_required(login_url='/')
def VIEW_SESSION(request):
    session = Session.objects.all()
    context = {
        'session': session,
    }
    return render(request, 'hod/view_session.html', context)


@login_required(login_url='/')
def EDIT_SESSION(request, id):
    session = Session.objects.get(id=id)
    context = {
        'session': session,
    }
    return render(request, "hod/edit_session.html", context)


@login_required(login_url='/')
def UPDATE_SESSION(request):
    if request.method == "POST":
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')
        session_id = request.POST.get('session_id')

        session = Session.objects.get(id=session_id)

        session.session_start = session_start
        session.session_end = session_end
        session.save()
        messages.success(request, "Session updated successfully!")
        return redirect('view_session')

    return render(request, 'hod/edit_session.html')


@login_required(login_url='/')
def FACULTY_SEND_NOTIFICATION(request):
    faculty = Faculty.objects.all()
    faculty_notification = Faculty_notification.objects.all()
    context = {
        'faculty': faculty,
        'faculty_notification': faculty_notification
    }
    return render(request, "hod/faculty_send_notification.html", context)


@login_required(login_url='/')
def FACULTY_SAVE_NOTIFICATION(request):
    if request.method == "POST":
        faculty_id = request.POST.get('faculty_id')
        f_name = request.POST.get('faculty_name')
        message = request.POST.get('message')
        faculty = Faculty.objects.get(admin=faculty_id)
        notification = Faculty_notification(
            faculty_id=faculty,
            message=message,
            f_name=f_name,
        )
        notification.save()
        messages.success(request, "Message sent Successfully!")
        return redirect('faculty_send_notification')
    return None


@login_required(login_url='/')
def FACULTY_LEAVE(request):
    leave = Faculty_leave.objects.all()
    context = {
        'leave': leave,
    }
    return render(request, "hod/faculty_leave.html", context)


@login_required(login_url='/')
def ACCEPT_FACULTY_LEAVE(request, status):
    leave = Faculty_leave.objects.get(id=status)
    leave.status = 2
    leave.save()
    return redirect('faculty_leave')


@login_required(login_url='/')
def REJECT_FACULTY_LEAVE(request, status):
    leave = Faculty_leave.objects.get(id=status)
    leave.status = 1
    leave.save()
    return redirect('faculty_leave')


@login_required(login_url='/')
def READ_FACULTY_FEEDBACK(request):
    faculty_feedback = Faculty_feedback.objects.all()
    context = {
        'faculty_feedback': faculty_feedback,
    }
    return render(request, 'hod/faculty_feedback.html', context)


@login_required(login_url='/')
def REPLY_FACULTY_FEEDBACK(request):
    if request.method == "POST":
        faculty_id = request.POST.get('faculty_id')
        reply = request.POST.get('reply')
        feedback = Faculty_feedback.objects.get(id=faculty_id)
        feedback.feedback_reply = reply
        feedback.save()
        messages.success(request, "Reply sent successfully!")
        return redirect("read_faculty_feedback")


@login_required(login_url='/')
def STUDENT_SEND_NOTIFICATION(request):
    Student = student.objects.all()
    notifications = Student_notification.objects.all()
    context = {
        'Student': Student,
        'notifications': notifications
    }
    return render(request, "hod/student_notifications.html", context)


@login_required(login_url='/')
def STUDENT_SAVE_NOTIFICATION(request):
    if request.method == "POST":
        id = request.POST.get('student_id')
        message = request.POST.get('message')
        s_name = request.POST.get('student_name')
        Student = student.objects.get(admin=id)
        notification = Student_notification(
            student_id=Student,
            message=message,
            s_name=s_name,
        )
        notification.save()
        messages.success(request, "Notification Sent Successfully!")
        return redirect('student_send_notification')


@login_required(login_url='/')
def HOD_STUDENT_LEAVE(request):
    leave = Student_leave.objects.all()
    context = {
        'leave': leave
    }
    return render(request, 'hod/student_leave.html', context)


@login_required(login_url='/')
def ACCEPT_STUDENT_LEAVE(request, status):
    leave = Student_leave.objects.get(id=status)
    leave.status = 2
    leave.save()
    return redirect('hod_student_leave')


@login_required(login_url='/')
def REJECT_STUDENT_LEAVE(request, status):
    leave = Student_leave.objects.get(id=status)
    leave.status = 1
    leave.save()
    return redirect('hod_student_leave')


@login_required(login_url='/')
def READ_STUDENT_FEEDBACK(request):
    student_feedback = Student_feedback.objects.all()
    context = {
        'student_feedback': student_feedback,
    }
    print(student_feedback)
    return render(request, 'hod/student_feedback.html', context)


@login_required(login_url='/')
def REPLY_STUDENT_FEEDBACK(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        reply = request.POST.get('reply')
        feedback = Student_feedback.objects.get(id=student_id)
        feedback.feedback_reply = reply
        feedback.save()
        messages.success(request, "Reply sent successfully!")
        return redirect("read_student_feedback")
