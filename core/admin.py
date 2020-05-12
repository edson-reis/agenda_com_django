from django.contrib import admin
from core.models import ListaEvento
# Register your models here.

class ListaEventoAdmin(admin.ModelAdmin):
    list_display = ('titulo','data_evento','data_criacao')
    list_filter = ('titulo','usuario','data_evento',)

admin.site.register(ListaEvento, ListaEventoAdmin)

