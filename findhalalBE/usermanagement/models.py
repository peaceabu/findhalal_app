# usermanagement/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # You can add any additional fields here
    # For example, adding a field for additional info
    # additional_field = models.CharField(max_length=255, blank=True, null=True)
    pass
