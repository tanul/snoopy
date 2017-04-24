from django.contrib import admin
from blog.models import Category, Author, Article, Tag, Comment, Reply
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Article, ArticleAdmin)