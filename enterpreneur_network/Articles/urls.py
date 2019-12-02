from django.urls import path
from .import views
from .views import ArticleList, ArticleDetail, ContactUs

app_name = 'Articles'

urlpatterns = [
	path('articles/', ArticleList.as_view(), name='articles'),
	path('articles/<str:name>', views.article_category, name='article_category'),
	path('articles/<slug>/', ArticleDetail.as_view(), name = 'article-detail'),
	path('contactus/', ContactUs.as_view(), name='contact-us'),
	]
