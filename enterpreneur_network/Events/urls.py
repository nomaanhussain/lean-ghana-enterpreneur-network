from django.urls import path
from .views import event_show, CalendarView, EventDetailView, homepage, send_mail_view

app_name = 'Events'

urlpatterns = [
	path('startup-events/', event_show, name='startup-events'),
	path('startup-events/<slug>/', EventDetailView.as_view(), name = 'startup-event-detail'),
	path('calendar/', CalendarView, name='calendar'),
	path('', homepage, name='homepage'),
	path('send_email/<int:event_id>', send_mail_view, name='send_email'),
	]

