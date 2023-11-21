from django.contrib import admin

from users.models import Group, User
from django.contrib.auth.admin import UserAdmin as UserAdminStandart
# Register your models here.
admin.site.register(Group)

@admin.register(User)
class UserAdmin(UserAdminStandart):
    fieldsets = UserAdminStandart.fieldsets
    ADDITIONAL_USER_FIELDS = (
        (None, {'fields': ['group']}),
    )
    add_fieldsets = UserAdminStandart.add_fieldsets
    add_fieldsets += ADDITIONAL_USER_FIELDS
    fieldsets = fieldsets + ADDITIONAL_USER_FIELDS
    list_display = ['username', 'group', 'is_staff', 'is_superuser']

#admin.site.register(User, admin.ModelAdmin)

