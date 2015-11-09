from django.contrib import admin
from . import models


@admin.register(models.Communication)
class AuthorAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'
    list_display = [
        'name',
        'email',
        'date_created',
        'phone_number']


@admin.register(models.Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ['name', 'upload_file', 'date_created']
    readonly_fields = ['date_created']
