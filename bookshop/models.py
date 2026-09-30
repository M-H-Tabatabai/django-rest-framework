from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title

class MyBook(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    category = models.ManyToManyField(Category, related_name='books')
    published_date = models.DateField()

    def __str__(self):
        return self.title