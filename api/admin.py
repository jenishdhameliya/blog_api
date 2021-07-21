from django.contrib import admin
from .models import Article
# Register your models here.


# extra
# from .models import Snippet
# from django.contrib import admin
# from django.contrib.auth.models import Group

# admin.site.site_header = 'Admin panal modify'


# admin.site.register(Snippet)
# admin.site.register(Group)
# extra








# admin.site.register(Article)

@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('title', 'description')
    list_display     = ('title', 'description')
