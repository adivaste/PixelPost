from django.contrib import admin
from main.models import Account, Image
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class AccountInLine(admin.StackedInline):
      model = Account
      can_delete = False
      verbose_name_plural = 'Accounts'

class CustomizedAdmin(UserAdmin):
      inlines = (AccountInLine,)


# Register your models here
admin.site.unregister(User)
admin.site.register(User, CustomizedAdmin)
admin.site.register(Account)
admin.site.register(Image)