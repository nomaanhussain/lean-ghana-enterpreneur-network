from django.urls import path
from .views import event_show, CalendarView, EventDetailView, homepage

app_name = 'Events'

urlpatterns = [
	path('startup-events/', event_show, name='startup-events'),
	path('startup-events/<slug>/', EventDetailView.as_view(), name = 'startup-event-detail'),
	path('calendar/', CalendarView, name='calendar'),
	path('', homepage, name='homepage')
	]

