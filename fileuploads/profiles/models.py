from django.db import models


class UserModel(models.Model):
    image=models.ImageField(upload_to="images")