from django.db import models

# Create your models here.
class Blog(models.Model):
    """
    This is where i create the blog data components...Nermin
    Testing the GIT repository...llll
    This is to test the Git version control system
    """
    print("Hello")
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category')

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)