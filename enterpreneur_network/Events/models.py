from django.db import models
from django.contrib.auth.models import User	
from django.utils.timezone import now
from datetime import date
from django.core.exceptions import ValidationError
from django.shortcuts import reverse
from django.conf import settings


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip/Post Code', max_length=12,blank=True, null=True)

    VENUE_STATUS = (
		('on', 'Online'),
		('os', 'Onsite'),
		)
    venue_status_label = models.CharField(
		max_length=2,
		choices=VENUE_STATUS,
		default='os',
		help_text='Choose Venue either ONLINE or ONSITE',
		)


    class Meta:
        ordering = ['name']

    def check_status_venue(self):
    	if self.venue_status_label == 'on':
    		print("Trueeee")
    		return True
    	else:
    		return False
 
    def __str__(self):
        return self.name
 
 
class RegisteredUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.user.username


class Organizer(models.Model):
	name = models.CharField('Organizer Name', max_length=120)
	phone = models.CharField('Contact Phone', max_length=20)
	email_address = models.EmailField('Organizer Email')
	website = models.URLField('Web Address',blank=True, null=True)
	organizer_picture = models.ImageField(help_text="Add image of organizer")

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


class Category(models.Model):
    category_title = models.CharField(max_length=100, help_text="Add category of event")

    class Meta:
        ordering = ['category_title']

    def __str__(self):
        return self.category_title


class Event(models.Model):
	name = models.CharField('Event Name', max_length=120)
	day = models.DateField("Day of Event",default=now)
	start_time = models.TimeField("Starting Time",default=now)
	end_time = models.TimeField("Ending Time",default=now)
	picture = models.ImageField(help_text="Add picture related to event")
	description = models.TextField('Event Description')
	featured = models.BooleanField(default = False)
	categories = models.ManyToManyField(Category)
	cost = models.IntegerField(help_text="Add cost of event in case of free, write 0")
	venue = models.ForeignKey(Venue, on_delete=models.SET_NULL,null=True)
	event_manager = models.ManyToManyField(Organizer,blank =False)
	attendees = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
	slug = models.SlugField()
	EVENT_STATUS = (
		('o', 'On Time'),
		('d', 'Delayed'),
		('c', 'Completed'),
		)

	Event_Show = (
        ('e', 'Enable Event'),
        ('d', 'Disable Event'),
    )

	label = models.CharField(
		max_length=1,
		choices=EVENT_STATUS,
		default='o',
		help_text='Choose Event Status from here',
		)
	Event_Show_Status = models.CharField(max_length=1,choices=Event_Show,default='e',help_text='Either ENABLE and DISABLE your event')

	def get_absolute_url(self):
		return reverse('Events:startup-event-detail', kwargs = {'slug':self.slug})

	class Meta:
		ordering = ['-day']

	def clean(self):
		if self.end_time <= self.start_time:
			raise ValidationError('Ending times must after starting times')
		
	def __str__(self):
		return self.name

class Slides(models.Model):
	pic = models.ImageField(default=True)

class YoutubeUrl(models.Model):
	url = models.URLField(help_text="Enter Youtube Url")
