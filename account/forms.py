from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

import re  # regex


# Fields Here
code = 'ssad3003_signup'


# Forms Here
class SignUpForm(UserCreationForm):
    code = forms.CharField(
        max_length=30, required=True,
        validators=[
            RegexValidator(r'\b' + re.escape(code) + r'\b$')
        ]
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
