from django.contrib import admin
from .models import Quest

@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    list_display = ('str_1', 'str_2', 'str_3', 'str_4', 'str_5')