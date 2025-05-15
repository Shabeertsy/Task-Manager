from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class RoleChoices(models.TextChoices):
    ADMIN = 'Admin', 'Admin'
    SUPER_ADMIN = 'Super Admin', 'Super Admin'
    USER = 'User', 'User'



class Profile(AbstractUser):
    role = models.CharField(max_length=20, choices=RoleChoices.choices,null=True, blank=True)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
        ordering = ['-created_at']
      