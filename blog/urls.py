from django.conf.urls import url

from . import views

urlpatterns = [
	#ex: /blog/
	url(r'^$', views.index, name='index'),
	#ex: /blog/view/<slug>/
	url(r'^view/(?P<slug>[^\.]+).html', views.view_article, name='view_blog_article'),
	#ex: /blog/category/<slug>/
	url(r'^category/(?P<slug>[^\.]+).html', views.view_category, name='view_blog_category'),
]