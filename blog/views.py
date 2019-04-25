from django.shortcuts import render

# Create your views here.

# created a function (def) called post_list that takes request and will return the value it gets from calling another
# function render that will render (put together) our template blog/post_list.html
# blog/post_list.html

# def post_list(request):
#     return render(request, 'templates/blog/post_list.html', {})

# it gets to the templates auto' way.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

