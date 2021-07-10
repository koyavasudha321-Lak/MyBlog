from django.contrib import admin
from blog.models import Category,Post,Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'is_published', 'posted_at')
	list_filter = ('is_published', 'posted_at')
	list_editable = ('is_published',)  

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'is_resolved', 'commented_at')
	list_filter = ('is_resolved', 'commented_at')
	list_editable = ('is_resolved',)  




admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)


