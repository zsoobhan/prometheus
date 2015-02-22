from django.contrib import admin
from . import models


@admin.register(models.BlogEntry)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date_created'
    search_fields = ['slug', 'title', 'date_created', 'date_published']
    list_filter = ['status']
    list_display = [
        'slug',
        'status',
        'date_created',
        'date_published']
