from django.contrib import admin
from . import models

# Register your models here.
class Tas(admin.ModelAdmin):
    list_display = ('task','is_completed', 'updated_at')
    search_fields = ('task',)
    

admin.site.register(models.Employee)
admin.site.register(models.Todo, Tas)