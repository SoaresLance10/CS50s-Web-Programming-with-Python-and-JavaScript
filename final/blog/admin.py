from django.contrib import admin
from .models import User, Poster, Posts, Comment
# Register your models here.

admin.site.register(User)
admin.site.register(Poster)
admin.site.register(Posts)
admin.site.register(Comment)
