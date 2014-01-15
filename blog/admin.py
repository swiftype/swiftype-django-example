from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ['title']
	list_filter = ['created']
	search_fields = ['title', 'content']
	save_on_top = True
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
