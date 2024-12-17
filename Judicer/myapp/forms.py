from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# Custom User Creation Form
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

# Custom Authentication Form
class CustomAuthenticationForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=255, required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        # Validate email and password combination
        if email and password:
            user = CustomUser.objects.filter(email=email).first()
            if not user:
                raise forms.ValidationError("Invalid email or password.")
        return cleaned_data
