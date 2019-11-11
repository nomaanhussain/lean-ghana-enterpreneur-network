from django.contrib import admin
from Events.models import Event, Venue, Organizer, RegisteredUser, Category

admin.site.register([RegisteredUser, Category])

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ('name', 'event_date', 'venue', 'event_manager', 'label')
	list_filter = ('event_date', 'label', 'featured',)
	search_fields = ['name', 'cost', 'categories__category_title', 'event_manager__name']


@admin.register(Venue)
class VenuAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'zip_code')


@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
	list_display = ('name', 'email_address')
