from django.contrib import admin

from .models import Post, Comment,Email


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Email)