
from datetime import datetime, timedelta
from calendar import HTMLCalendar
from Events.models import Event

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year  #year
		self.month = month  #month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(day__day=day)
		print("events_per_day ",events_per_day )
		d = ''
		for event in events_per_day:
			a = event.get_absolute_url()
			print("aaa",a)
			# d += f'<a href="">a</a>'
			d = f'''
			<a href="" data-toggle="modal" data-target="#{event.name}">
			event</a>
			<div class="modal fade" id="{event.name}" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
				<div class="modal-dialog modal-dialog-centered" role="document"><div class="modal-content">
					<div class="modal-header"><h5 class="modal-title" id="exampleModalLongTitle">Modal title</h5>
						<button type="button" class="close" data-dismiss="modal" aria-label="Close">
						<span aria-hidden="true">&times;</span>
						</button>
					</div>
					<div class="modal-body"><p>{event.name}</p>
					<h5 class="text-info">{event.day}</h5>
					<a class="btn btn-info m-5" href="{a}">View Details</a>
						
  
					</div>
					</div>
				</div>
			</div>
			''' # circle

		if day != 0:
			if d =='':
				return f"<td style='text-align:center;'><span class='date'>{day}</span> {d} </td>"
			else:
				return f"<td id='d1' style='text-align:center;'><span class='date'>{day}</span> <br>{d} </td>"
		return '<td></td>'

	# formats a week as a tr 
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(day__year=self.year, day__month=self.month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal