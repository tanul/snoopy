from django.contrib import admin
from blog.models import Category, Author, Article, Tag, Comment, Reply
from django import forms
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget

#Creating CK editor pageform
class CategoryAdminForm(ModelForm):
	description = forms.CharField(widget=CKEditorWidget())
	class Meta:
		model = Category

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}

class CategoryAdmin(admin.ModelAdmin):
	form = CategoryAdminForm
	fields = ['title', 'description', 'slug']
	prepopulated_fields = {'slug':('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Article, ArticleAdmin)