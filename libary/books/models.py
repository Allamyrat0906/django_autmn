from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Country(models.Model):
    name_c = models.CharField(max_length=100)
    short_code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name_c} {self.short_code}"

    class Meta:
        verbose_name_plural = "Yurtlar"


class Address(models.Model):
    street = models.CharField(max_length=100)
    post_code = models.IntegerField(max_length=7)

    def __str__(self):
        return f"{self.street} {self.post_code}"


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def full_name(self):
        return f"{self.name}{self.surname}"

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=255)
    rating = models.IntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)
    ])
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    adress = models.OneToOneField(
        Address, on_delete=models.SET_NULL, null=True)
    country = models.ManyToManyField(Country,)
    is_bestseller = models.BooleanField(default=False)
    slug = models.SlugField(null=False, blank=True)

    def __str__(self):
        return f"{self.title} {self.author}"

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def save(self, *args, **kwargs,):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
