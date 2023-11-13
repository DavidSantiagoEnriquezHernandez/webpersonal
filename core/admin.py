from django.contrib import admin
from .models import Work

from django import forms


class WorkAdminForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = '__all__'
class WorkAdmin(admin.ModelAdmin):
    form = WorkAdminForm

    
# Register your models here.
admin.site.register(Work, WorkAdmin)

