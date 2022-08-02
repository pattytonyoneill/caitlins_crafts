from django.contrib import admin
from .models import Crafts, Category


class CraftsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Crafts, CraftsAdmin)
admin.site.register(Category, CategoryAdmin)
