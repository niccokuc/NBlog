from Blogs.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404, render

"""
The view is where you do all the logic to be sent to your templates.
In this example we will not be dealing with RequestContext.
This would give you access to the request object which contains details
for the currently logged in user, as well as a few other features you
will be likely to use in the future.

For this example we need to create 3 views.

Display your categories & latest posts
Display the posts in a specific category
Display the post
Here is a copy of the view.py.
"""

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

def view_post(request, slug):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })