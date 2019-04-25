# define url for the blog app , we wuold like to keep the main my_site/url clean , and import the url from blog, that
# is more modular

# Import the path and url to our application.
from django.urls import path
from . import views

# post_list it is an example of view which in the application directory view.py (blog application)
# The last part, name='post_list', is the name of the URL that will be used to identify the view.
urlpatterns = [
    path('', views.post_list, name='post_list'),
]



