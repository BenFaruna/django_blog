from django.contrib import admin

from .models import BlogPost, Comment


class CommentInLine(admin.TabularInline):
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]


# Register your models here.
admin.site.register(BlogPost, ArticleAdmin)
admin.site.register(Comment)
