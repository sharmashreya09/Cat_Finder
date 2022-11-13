from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=70, blank=True, unique=True)
    message = models.TextField()

    def __str__(self):
        return self.email
