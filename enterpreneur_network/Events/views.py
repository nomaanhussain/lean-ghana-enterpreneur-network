# from urllib.parse import quote_plus
from requests.utils import requote_uri
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (ListView,DetailView,View)
from Events.models import Event
from Articles.models import Article
# import datetime
from django.core.exceptions import ObjectDoesNotExist
from Events.forms import EventSearch
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from datetime import datetime, timedelta, date
from django.contrib.auth.decorators import login_required
# from django.views import generic
from django.utils.safestring import mark_safe
from .models import *
from .utils import Calendar
import calendar
from django.contrib import messages
from django.conf import settings
from django.contrib import admin
from django.core.mail import send_mail, BadHeaderError
from Events.forms import WebinarMailForm

def homepage(request):
	featured = Article.objects.filter(featured='True', status__exact='p').order_by('-timestamp')[0:3]
	latest = Article.objects.filter(status__exact='p').order_by('-timestamp')[0:3]
	month_event = Event.objects.filter( Event_Show_Status__exact='e',label='o').order_by('day')[0:2]
	print("month_event",month_event)
	event_one = month_event[0]
	event_two = month_event[1]

	context = {
		'featured':featured,
		'latest' :latest,
		'event_one': event_one,
		'event_two':event_two
	}
	return render(request,'Events/Homepage.html',context)


def event_show(request):
	form = EventSearch()
	date = datetime.now()
	month_event = Event.objects.filter(day__year=date.year, day__month=date.month, 
		Event_Show_Status__exact='e',label='o').order_by('day')
	share_string = month_event
	if request.method == 'POST':
		form = EventSearch(request.POST)
		if form.is_valid():
			date = form.cleaned_data['date']
			month_event = Event.objects.filter(day__year=date.year, day__month=date.month,
				Event_Show_Status__exact='e',label='o').order_by('day')
			share_string = month_event
	return render(request,'Events/Event_list.html',{'form':form,'month_event':month_event,'date':date,'share_string':share_string})


class EventDetailView(DetailView):
	model = Event
	template_name = 'Events/Event_detail.html'
	context_object_name = 'event'

	
	def post(self, request, *args, **kwargs):
		if self.request.user.is_authenticated:
			event = get_object_or_404(Event , slug = self.kwargs.get('slug'))
			name = request.user.pk
			list_of_attendess = event.attendees.all()
			print('list_of_attendess',list_of_attendess)
			if request.user in list_of_attendess:
				messages.info(request,"You are already registered")
				return redirect("Events:startup-event-detail" , slug = self.kwargs.get('slug'))
			else:
				event.attendees.add(name) #takes pk as arg (ManyToManyField)
				messages.info(request,"Thanks for registration")
				return redirect("Events:startup-event-detail" , slug = self.kwargs.get('slug'))
		else:
			messages.info(request,"login required")
			return redirect("/accounts/login/")

	
		




def CalendarView(request):
	events = Event.objects.all()
	# d = get_date(request.GET.get('day', None))
	d = get_date(request.GET.get('month', None))
	cal = Calendar(d.year, d.month)
	html_cal = cal.formatmonth(withyear=True)
	print("html_calllll", mark_safe(html_cal))
	context = {'events':events,'calendar':mark_safe(html_cal),'prev_month':prev_month(d),'next_month':next_month(d)}
	return render(request,'Events/cal.html',context)


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def send_mail_view(request,event_id):
		if request.user.is_superuser:
			header = admin.site.site_header
			event_id = event_id
			event = get_object_or_404(Event , pk = event_id)
			list_of_attendess = event.attendees.all()
			form = WebinarMailForm()
			message = ''
			if request.method == 'POST':
				form = WebinarMailForm(request.POST)
				if form.is_valid():
					subject = form.cleaned_data['Subject']
					content = form.cleaned_data['Content']
					event = get_object_or_404(Event , pk = event_id)
					name = request.user.pk
					list_of_attendess = event.attendees.all()
					emails = []
					for user in list_of_attendess:
						emails.append(user.email)
					try:
						message = "Sent Successfully"
						send_mail(subject,content,settings.EMAIL_HOST_USER,emails,fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
			return render(request,'Events/send_email.html', {'form':form,'event_id':event_id,'total_attendees':len(list_of_attendess),'header':header,'message':message} )
		else:
			raise Http404("Only admin can view this page")


# class ContactForm(View):
# 	form_class = ContactForm
# 	template_name = 'Events/ContactUs.html'

# 	def get(self,request):
# 		pass

# 	def post(self,request):
# 		pass