from django.contrib import admin
from .models import resultado

@admin.register(resultado)
class resultadoAdmin(admin.ModelAdmin):
    list_display = ('res',)