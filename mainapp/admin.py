from django.contrib import admin
from .models import Teacher
from .models import Department
# Register your models here.
from django.contrib import admin
from .models import Alumni
from .models import Notification
admin.site.register(Notification)
admin.site.register(Alumni)
admin.site.register(Teacher)
admin.site.register(Department)
from django.contrib import admin



