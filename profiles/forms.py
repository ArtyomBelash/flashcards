from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from profiles.models import Profile


class ProfileForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('usable_password', None)

    email = forms.EmailField(label='Email')
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'date_of_birth')

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        date_of_birth = self.cleaned_data['date_of_birth']
        profile = Profile(user=user, email=user.email, date_of_birth=date_of_birth)
        profile.save()
        return user
