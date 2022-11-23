from django.contrib import admin

from blog.models import Categoria, Post, Info, Contacto

# Register your models here.

admin.site.register(Categoria),
admin.site.register(Post),
admin.site.register(Info),
admin.site.register(Contacto),