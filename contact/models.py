from django.db import models

# Create your models here.
class Contact(models.Model):
    firstName = models.CharField(max_length=90)
    lastName = models.CharField(max_length=90)
    email = models.CharField(max_length=200)
    content = models.TextField(null=True)

    def __str__(self):
        return f"{self.email}"

