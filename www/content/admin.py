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
