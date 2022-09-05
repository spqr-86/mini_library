from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

CustomUser = get_user_model()


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'username', 'phone_number', 'full_name']


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = '__all__'
