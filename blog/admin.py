from django.contrib import admin

# Register your models here.
# we register the model (djuango object) .
from django.contrib import admin
from .models import Post

# we register the model (djuango object) .
admin.site.register(Post)