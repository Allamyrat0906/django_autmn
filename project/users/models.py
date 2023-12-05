from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=190)
    age=models.IntegerField(max_length=10)
    gender=models.CharField(max_length=10)
    email=models.EmailField(max_length=250)
    photo=models.ImageField(upload_to="images")
    country=models.CharField(max_length=100)
    dob=models.DateField(default=None)

    def __str__(self):
        return self.name