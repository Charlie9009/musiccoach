from django.contrib import admin
from .models import Exercise

# Register your models here.


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('date', 'get_type_display', 'time')
    list_filter = ('type', 'date')
    search_fields = ('description', 'notes')
