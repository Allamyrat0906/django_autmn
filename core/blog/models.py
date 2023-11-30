from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
        

    options=(
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category=models.ForeignKey(Category,on_delete=models.PROTECT,default=1)
    title=models.CharField(max_length=100)
    expert=models.TextField(max_length=250)
    content=models.TextField()
    slug=models.SlugField(max_length=250, unique_for_date='published')
    published=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='blogusers',
                             null=True)
    status=models.CharField(max_length=250,choices=options,default='published')
    objects=models.Manager()
    postobjects=PostObjects()

    class Meta:
        ordering=('-published',)

    def __str__(self):
        return f"{self.title} {self.author}"