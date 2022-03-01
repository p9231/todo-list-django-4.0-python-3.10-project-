from django.contrib import admin
from todoapp.models import TODO

class AdminView(admin.ModelAdmin):
    todo_display=['title', 'descriptions','date_time', 'created_on', 'updated_on']

admin.site.register(TODO, AdminView)
