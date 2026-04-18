from django.contrib import admin
from .models import Alumni, Teacher, Department, Notification

class AlumniAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_email', 'department', 'role')

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email

admin.site.register(Alumni, AlumniAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Department)
admin.site.register(Notification)


