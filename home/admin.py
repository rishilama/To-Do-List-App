from django.contrib import admin
from . models import Tasks

# Register your models here.

class TasksAdmin(admin.ModelAdmin):
    list_display=['title','description']
admin.site.register(Tasks,TasksAdmin)