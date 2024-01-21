from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model): #კატეგორიების ცრილი
    name = models.CharField(max_length=100)
    text_color = models.CharField(max_length=50)
    background_color = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Data(models.Model): #ბლოგების ცრილი
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField()
    publish_date = models.DateTimeField() 
    categories = models.ManyToManyField(Category)
    email = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title

