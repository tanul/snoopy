from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import Category, Author, Article

# Create your views here.
def index(request):
	return render_to_response('blog/index.html', {'categories': Category.objects.all(), \
		'articles': Article.objects.all()[:5]})

def view_article(request, slug):
	return render_to_response('blog/view_post.html', {\
		'article': get_object_or_404(Article, slug=slug)})

def view_category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	return render_to_response('blog/view_category.html', \
		{'category':category, \
		'articles': Article.objects.filter(category=category)[:5]})

