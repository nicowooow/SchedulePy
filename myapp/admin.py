from django.contrib import admin
from myapp.models import Profile, Project, Task
# Register your models here.

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Task)