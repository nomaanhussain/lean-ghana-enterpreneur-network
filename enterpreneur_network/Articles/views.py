from django.shortcuts import render
from django.views.generic import (ListView,DetailView,View)
from .models import Article, Category
from Articles.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.views.generic.base import TemplateView

class ArticleList(ListView):
	model = Article
	paginate_by = 10
	template_name = 'Articles/Articles_list.html'
	context_object_name = 'articles'

	def get_queryset(self):
		return Article.objects.filter(status__exact='p').order_by('-timestamp')

	def get_context_data(self,**kwargs):
		context = super(ArticleList,self).get_context_data(**kwargs) #returns a dictionary of context
		new_context_objects = {'Categories':Category.objects.all()}
		context.update(new_context_objects)
		return context 

def article_category(request,name):
	Articles = Article.objects.filter(categories__category_title=name, status__exact='p')
	context = {'Articles':Articles,'name':name}
	return render(request , 'Articles/articles_category.html',context)

class ArticleDetail(DetailView):
	model = Article
	template_name = 'Articles/Articles_detail.html'
	context_object_name = 'article_detail'

	def get_context_data(self,**kwargs):
		context = super(ArticleDetail,self).get_context_data(**kwargs)
		m = self.kwargs.get('slug')
		for i in Article.objects.filter(slug = m):
			a = i.categories.all()[0]
		q = Article.objects.filter(categories = a)[0:3]
		new_context = {'categories':q}
		context.update(new_context)
		return context


class ContactUs(View):
	form_class = ContactForm
	template_name = 'Articles/contact_us.html'

	def get(self,request):
		form = self.form_class()
		return render (request,self.template_name,{'form':form})

	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			subject = 'Enterpreneur Network: Contact message from{}'.format(name)
			message = form.cleaned_data['message']
			send_mail(subject,message,email,[settings.EMAIL_HOST_USER],fail_silently=False)
			try:
				email_status = 'Thanks {} for contacting us'.format(name)
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return render (request,self.template_name,{'form':form,'email_status':email_status})
		else:
			email_status = 'Please provide correct data'
			return render (request,self.template_name,{'form':form,'email_status':email_status})

class AboutUs(TemplateView):
	template_name = 'Articles/about_us.html'
	



