from django.contrib import admin
from .models import Post, Comment


# Register your models here.
class Commentinline(admin.TabularInline):
    model = Comment
    extra = 2


class PostAdimin(admin.ModelAdmin):
    fieldsets=[
      

    ]
    inlines=[Commentinline]
    list_display = ('title','approved_comments_counts', 'published_date')
    list_filter = ['published_date']
    search_fields = ['title']
admin.site.register(Post, PostAdimin)
admin.site.register(Comment)