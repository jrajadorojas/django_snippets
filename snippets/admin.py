from django.contrib import admin

from .models import Language


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    list_filter = ('name','slug')
    search_fields = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}
