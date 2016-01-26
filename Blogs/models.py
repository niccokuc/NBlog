from django.db import models
from django.db.models import permalink

# Create your models here.
# This is the blog model.as
# Two models created: A BLOG and CATEGORY model.

class Blog(models.Model):
    """
    This creates a database table with the name "Blog".
    This needs to be something obvious and will be used a lot.
    This is a simple blog model.
    These are basic fields to be created in your database.
    """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    #category = models.ForeignKey('blog.Category')

    def __str__(self):
        """
        The __str__ function sets the text reference for each record.
        This is used mainly in the automated django admin, but this is still available to use on your own site.
        :return: title
        """
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        """
        The get_absolute_url function defines a URL, again used in the admin area, for each record.
        :return:Without the @permalink decorator the following would not work.
        This returns a URL calculated from the urls.py file which will be explained shortly.
        I would recommend using this method as it allows you to change the URL for a page in only one location.
        """
        return ('view_blog_post', None, { 'slug': self.slug })


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    def __str__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })