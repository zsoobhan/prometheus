from django.contrib import admin
from . import models


@admin.register(models.BlogEntry)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['slug', 'title', 'date_created', 'date_published']
    list_filter = ['status']
    list_display = [
        'slug',
        'status',
        'date',
        'date_published',
        'is_active']


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['slug', 'title', 'date_created', 'blurb']
    list_display = [
        'slug',
        'title',
        'date_created']
