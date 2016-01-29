from django.contrib import admin
from .models import Blog, Category

"""
In many of your own applications you will probably want to write your own administration
functions, you will completely miss out this section.

Create admin.py in blog folder we created earlier.
This admin.py file is automatically checked by django admin for
every application defined under INSTALLED_APPS in the settings.py
Adding change to detect
Testing 123
Test 0.0.11
"""

"""
teswt123
Register our models Blog & Category with the admin
"""

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog)
admin.site.register(Category)