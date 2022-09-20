from django.contrib import admin
from .models import Welcome


@admin.register(Welcome)
class WelcomeAdmin(admin.ModelAdmin):
    list_display = ("sentence", )
