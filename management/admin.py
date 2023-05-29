from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class UserModel(UserAdmin):
    list_display = ['username', 'user_type']


admin.site.register(CustomUser, UserModel)
admin.site.register(Course)
admin.site.register(Session)
admin.site.register(student)
admin.site.register(Faculty)
admin.site.register(Subject)
admin.site.register(Faculty_notification)
admin.site.register(Faculty_leave)
admin.site.register(Faculty_feedback)
admin.site.register(Student_notification)
admin.site.register(Student_feedback)
admin.site.register(Student_leave)
admin.site.register(Attendence)
admin.site.register(Attendence_report)
