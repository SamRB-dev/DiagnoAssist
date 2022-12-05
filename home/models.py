from django.db import models

# Create your models here.
class Table(models.Model):
    UID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    dob = models.DateField(default=None)
    email = models.EmailField(default=None)
    password = models.CharField(max_length=16,default=None)
    status = models.CharField(max_length=20,default="pending")

    def __str__(self):
        return self.name