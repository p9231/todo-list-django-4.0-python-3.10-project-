from django.contrib import admin
from todoapp.models import TODO
from import_export.admin import ImportExportModelAdmin

# class AdminView(admin.ModelAdmin):
#     todo_display=('title', 'descriptions','date_time', 'created_on', 'updated_on')

# admin.site.register(TODO, AdminView)
@admin.register(TODO)
class CSV_deal(ImportExportModelAdmin):
    pass
