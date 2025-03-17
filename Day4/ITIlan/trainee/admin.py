from django.contrib import admin
from .models import Trainee
class TraineeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ['name', 'email']
    ordering = ('name',)
# Register your models here.
admin.site.register(Trainee, TraineeAdmin)