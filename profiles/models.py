from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email = models.EmailField(unique=True, blank=False, null=False)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username
