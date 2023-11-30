from django.contrib import admin

from profiles.models import UserModel


class UserP(admin.ModelAdmin):
    list_filter=("image",)
admin.site.register(UserModel,UserP)