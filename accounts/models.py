from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class UserType(models.TextChoices):
    CUSTOMER = 'customer', 'مشتری'
    ADMIN = 'admin', 'مدیر'


