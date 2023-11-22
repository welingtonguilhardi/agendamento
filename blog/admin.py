from django.contrib import admin
from .models import Post,ComentarioPost,CurtidaPost


admin.site.register(Post)
admin.site.register(CurtidaPost)
admin.site.register(ComentarioPost)
