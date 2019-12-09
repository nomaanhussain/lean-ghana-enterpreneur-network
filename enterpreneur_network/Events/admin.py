from django.contrib import admin
from Events.models import Event, Venue, Organizer, RegisteredUser, Category,Slides ,YoutubeUrl
from django.template.response import TemplateResponse
from django.urls import path
from Events.forms import WebinarMailForm
from django.shortcuts import render ,get_object_or_404
from django.http import Http404
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
admin.site.register([RegisteredUser, Category,Slides,YoutubeUrl])
from django.http import HttpResponse, HttpResponseRedirect


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ('name', 'day', 'venue', 'label')
	list_filter = ('day', 'label', 'featured','Event_Show_Status','venue__venue_status_label',)
	search_fields = ['name','day', 'cost', 'categories__category_title', 'event_manager__name','venue__venue_status_label'] #incomplete searc using venue
	actions = ['send_email']

	def send_email(self, request, queryset):
		if request.user.is_superuser:
			header = admin.site.site_header
			event_ids = queryset.values_list('pk', flat=True)
			print("idsss",event_ids)
			return HttpResponseRedirect('/send_email/%s' % (
                ','.join(str(pk) for pk in event_ids),
            ))
	# def get_urls(self):
	# 	urls = super().get_urls()
	# 	print("urlsss",urls)
		
	# 	my_urls = [
 #            path('<int:event_id>/send_email/', self.send_email, name='send_email'),
 #        ]
        
	# 	return my_urls + urls

	# def send_email(self, request,event_id ):
	# 	if request.user.is_superuser:
	# 		header = admin.site.site_header
	# 		event_id = event_id
	# 		event = get_object_or_404(Event , pk = event_id)
	# 		list_of_attendess = event.attendees.all()
	# 		form = WebinarMailForm()
	# 		message = ''
	# 		if request.method == 'POST':
	# 			form = WebinarMailForm(request.POST)
	# 			if form.is_valid():
	# 				subject = form.cleaned_data['Subject']
	# 				content = form.cleaned_data['Content']
	# 				event = get_object_or_404(Event , pk = event_id)
	# 				name = request.user.pk
	# 				list_of_attendess = event.attendees.all()
	# 				emails = []
	# 				for user in list_of_attendess:
	# 					emails.append(user.email)
	# 				try:
	# 					message = "Sent Successfully"
	# 					send_mail(subject,content,settings.EMAIL_HOST_USER,emails,fail_silently=False)
	# 				except BadHeaderError:
	# 					return HttpResponse('Invalid header found.')
	# 		return render(request,'admin/send_email.html', {'form':form,'event_id':event_id,'total_attendees':len(list_of_attendess),'header':header,'message':message} )
	# 	else:
	# 		raise Http404("Only admin can view this page")



@admin.register(Venue)
class VenuAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'zip_code')
	search_fields = ['name','zip_code']


@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
	list_display = ('name', 'email_address')
	search_fields = ['name']



#http://127.0.0.1:8000/admin/Events/event/2/send_email/