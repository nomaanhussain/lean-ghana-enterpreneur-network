from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (ListView,DetailView,View)
from Events.models import Event
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

def homepage(request):
	return render(request,'Events/Homepage.html')


def event_show(request):
	form = EventSearch()
	date = datetime.now()
	month_event = Event.objects.filter(day__year=date.year, day__month=date.month, 
		Event_Show_Status__exact='e').order_by('day')
	if request.method == 'POST':
		form = EventSearch(request.POST)
		if form.is_valid():
			date = form.cleaned_data['date']
			month_event = Event.objects.filter(day__year=date.year, day__month=date.month)
	return render(request,'Events/Event_list.html',{'form':form,'month_event':month_event,'date':date})


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
				message = "You are already registered"
			else:
				event.attendees.add(name) #takes pk as arg (ManyToManyField)
				message = "Thanks for registration"
			return HttpResponse(message)
		else:
			message = "login required"
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



# class ContactForm(View):
# 	form_class = ContactForm
# 	template_name = 'Events/ContactUs.html'

# 	def get(self,request):
# 		pass

# 	def post(self,request):
# 		pass