
from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.

# created a function (def) called post_list that takes request and will return the value it gets from calling another
# function render that will render (put together) our template blog/post_list.html
# blog/post_list.html

# def post_list(request):
#     return render(request, 'templates/blog/post_list.html', {})




"""
# it gets to the templates auto' way.
# request -  everything we receive from the user via the Internet 
#  giving the template file ('blog/post_list.html'). The last parameter, {}, is a place in which we can add some things
#  for the template to use. We need to give them names (we will stick to 'posts' right now). :) It should look like
#  this: {'posts': posts}. Please note that the part before : is a string; you need to wrap it with quotes: ''
"""
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

