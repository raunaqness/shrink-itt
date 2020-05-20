from django.contrib import admin
from .models import URLs
# Register your models here.

class URLAdmin(admin.ModelAdmin):

    list_display = ("shrinked_url", "complete_url", "created",)

admin.site.register(URLs, URLAdmin)