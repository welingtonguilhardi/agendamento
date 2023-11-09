from django.contrib import admin
from . models import Users
from django.contrib.auth import admin as auth_admin


admin.site.register(Users)


# @admin.register(Users)
# class UsersAdmin(auth_admin.UserAdmin):
#     fieldsets = auth_admin.UserAdmin.fieldsets + (("Informações pessoais", {"fields": ("cpf",) } ),)