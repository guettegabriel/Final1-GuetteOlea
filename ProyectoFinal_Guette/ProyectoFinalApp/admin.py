from django.contrib import admin

from .models import *

# Register your models here.

class SegaAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'genero')
    search_fields = ('nombre', 'genero')


class GameBoyAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'genero')
    search_fields = ('nombre', 'genero')

class NesAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'genero')
    search_fields = ('nombre', 'genero')





admin.site.register(Sega, SegaAdmin)
admin.site.register(GameBoy, GameBoyAdmin)
admin.site.register(Nes, NesAdmin)
admin.site.register(Profile)

# admin, admin -> python manage.py createsuperuser