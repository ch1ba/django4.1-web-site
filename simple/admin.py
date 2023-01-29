from django.contrib import admin

from .models import *

# Register your models here.

class SimpleAdmin(admin.ModelAdmin):
    list_filter = ("time_create","is_published")
    list_display = ("id","title","time_create","photo","is_published")
    list_display_links = ("id","title")
    search_fields = ("title","content")
    list_editable = ("is_published",)

admin.site.register(Simple,SimpleAdmin)
