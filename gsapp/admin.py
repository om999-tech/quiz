from django.contrib import admin
from .models import Register_std,IsFormActive


@admin.register(Register_std)
class RegisterStdAdmin(admin.ModelAdmin):
    list_display =['name','father_name','mobile_no','gender','email','address']
    list_filter = ['gender']


@admin.register(IsFormActive)
class IsFormactivAdmin(admin.ModelAdmin):
    list_display =['active_status']