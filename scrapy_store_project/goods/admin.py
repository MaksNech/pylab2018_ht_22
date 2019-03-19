from django.contrib import admin

from .models import Bag


class BagAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand')
    list_filter = ('brand',)
    search_fields = ('title', 'brand')

admin.site.register(Bag, BagAdmin)

