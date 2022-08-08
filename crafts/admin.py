from django.contrib import admin
from .models import Crafts, Category


class CraftsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Crafts, CraftsAdmin)
admin.site.register(Category, CategoryAdmin)
