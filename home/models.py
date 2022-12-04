from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    dob = models.DateTimeField()
    email = models.EmailField()
    password = models.CharField(max_length=16)
    picture = models.ImageField(upload_to=f"media/{uid}/picture",width_field=350,height_field=350)
    license = models.FileField(upload_to=f'media/{uid}/license/',default=None)
    status = models.CharField(max_length=20,default="pending")

    def __str__(self):
        return f"[{self.uid}] {self.name}"
