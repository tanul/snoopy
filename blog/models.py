from django.db import models
from django.db.models import permalink
from tinymce.widgets import TinyMCE

# Create your models here.
class Category(models.Model):
	title = models.CharField(max_length=200, db_index=True)
	description = models.CharField(max_length=400)
	slug = models.SlugField(max_length=400, db_index=True)

	def __str__(self):
		return self.title

	def __unicode__(self):
		return '%s' % self.title

	@permalink
	def get_absolute_url(self):
		return ('view_blog_category', None, {'slug': self.slug})

class Tag(models.Model):
	tagname = models.CharField(max_length=50)
	description = models.CharField(max_length=200, default="self explainable")

	def __str__(self):
		return self.tagname

class Author(models.Model):
	name = models.CharField(max_length=100)
	member_since = models.DateTimeField('Member Since')

	def __str__(self):
		return self.name

class Article(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=400, unique=True)
	description = models.CharField(max_length=400)
	body = models.TextField()
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	pub_date = models.DateTimeField('date published')
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.title

	def __unicode__(self):
		return '%s' % self.title

	@permalink
	def get_absolute_url(self):
		return ('view_blog_article', None, {'slug': self.slug})

class Comment(models.Model):
	comment_text = models.CharField(max_length=1000)
	comment_author = models.CharField(max_length=200, default="ANONYMOUS")
	article = models.ForeignKey(Article, on_delete=models.CASCADE)

class Reply(models.Model):
	reply_text = models.CharField(max_length=1000)
	reply_author = models.CharField(max_length=200, default="ANONYMOUS")
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


