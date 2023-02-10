from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    Clinic1 = models.CharField(max_length=200, unique=True)
    Clinic2 = models.CharField(max_length=200, unique=True)
    Clinic3 = models.CharField(max_length=200, unique=True)
    Clinic4 = models.CharField(max_length=200, unique=True)
    price1 = models.CharField(max_length=200, unique=True)
    price2 = models.CharField(max_length=200, unique=True)
    price3 = models.CharField(max_length=200, unique=True)
    price4 = models.CharField(max_length=200, unique=True)
    phone1 = models.CharField(max_length=200, unique=True)
    phone2 = models.CharField(max_length=200, unique=True)
    phone3 = models.CharField(max_length=200, unique=True)
    phone4 = models.CharField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(null=True, blank = True,upload_to='picture')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
