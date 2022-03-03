from django.contrib import admin
from todoapp.models import TODO
from import_export.admin import ImportExportModelAdmin


@admin.register(TODO)
class CSV_deal(ImportExportModelAdmin):
    pass
