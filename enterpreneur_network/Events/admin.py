from django.contrib import admin
from Events.models import Event, Venue, Organizer, RegisteredUser, Category

admin.site.register([RegisteredUser, Category])

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ('name', 'day', 'venue', 'label')
	list_filter = ('day', 'label', 'featured','Event_Show_Status',)
	search_fields = ['name','day', 'cost', 'categories__category_title', 'event_manager__name']
	

@admin.register(Venue)
class VenuAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'zip_code')
	search_fields = ['name','zip_code']


@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
	list_display = ('name', 'email_address')
	search_fields = ['name']



