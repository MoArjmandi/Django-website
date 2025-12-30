from django.db import models
from django.contrib.auth import get_user_model



user = get_user_model()
# Create your models here.




class ContactModel(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(default=None , null=True)
    phonenumber= models.CharField(max_length=200, blank=True , null= True)
    subject = models.CharField(max_length=200, blank=True , null= True)
    content = models.TextField(max_length=700)
    is_seen = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.full_name