from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# from jupyterlab_server import slugify

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=100)
    pages = models.IntegerField(default=0)
    raiting = models.IntegerField(max_length=125)
    slug = models.SlugField(null=False, default="", db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def __str__(self):
        return f"{self.title} , {self.pages}"
