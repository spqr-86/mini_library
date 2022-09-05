from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('username', 'email', 'full_name', 'phone_number')
    readonly_fields = ('last_login', 'date_joined',)
    fieldsets = (
        (None, {'fields': ('username',
                           'phone_number',
                           'full_name',
                           )}),
        ('Personal info', {'classes': ('wide',), 'fields': ('email',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined',)})
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'username',
         'password1', 'password2', 'first_name')}),
    )


admin.site.register(User, CustomUserAdmin)
