from django.contrib import admin
from .models import*

# Register your models here.
@admin.register((RegistrationForm))
class RegistrationAdmin(admin.ModelAdmin):
    list_display=("id","first_name","last_name","phone","email","course","state")