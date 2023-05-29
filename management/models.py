from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    USER = (
        (1, 'HOD'),
        (2, 'FACULTY'),
        (3, 'STUDENT'),
    )

    user_type = models.CharField(choices=USER, max_length=60, default=1)
    profile_pic = models.ImageField(upload_to='media/profile-pic')


class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Session(models.Model):
    session_start = models.TextField(max_length=100)
    session_end = models.TextField(max_length=100)

    def __str__(self):
        return self.session_start + " - " + self.session_end


class student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField(max_length=200)
    father_name = models.TextField(max_length=100)
    phone_no = models.IntegerField()
    gender = models.CharField(max_length=20)
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    session_year_id = models.ForeignKey(Session, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name


class Faculty(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField(max_length=200)
    phone_no = models.IntegerField()
    gender = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Faculty_notification(models.Model):
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    f_name = models.TextField(default='None')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.faculty_id.admin.first_name + " " + self.faculty_id.admin.last_name


class Faculty_leave(models.Model):
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    date = models.DateField()
    message = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.faculty_id.admin.first_name + " " + self.faculty_id.admin.last_name


class Faculty_feedback(models.Model):
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.faculty_id.admin.first_name + " " + self.faculty_id.admin.last_name


class Student_notification(models.Model):
    student_id = models.ForeignKey(student, on_delete=models.CASCADE)
    s_name = models.TextField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.student_id.admin.first_name + " " + self.student_id.admin.last_name


class Student_leave(models.Model):
    student_id = models.ForeignKey(student, on_delete=models.CASCADE)
    date = models.DateField()
    message = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id.admin.first_name + " " + self.student_id.admin.last_name


class Student_feedback(models.Model):
    student_id = models.ForeignKey(student, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id.admin.first_name + " " + self.student_id.admin.last_name


class Attendence(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    date = models.DateField()
    session_year_id = models.ForeignKey(Session, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_id.name


class Attendence_report(models.Model):
    student_id = models.ForeignKey(student, on_delete=models.DO_NOTHING)
    attendence_id = models.ForeignKey(Attendence, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id.admin.first_name
