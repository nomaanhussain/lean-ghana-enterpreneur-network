from django import forms
# from future import unicode_literals
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime

class EventSearch(forms.Form):
	date = forms.DateField(input_formats=['%m-%Y'],
		widget=forms.DateInput(attrs={'id':'datepicker','readonly':'readonly','class':'date-own form-control',
			'style':'width: 300px',}
			,format='%m/%Y'))


class WebinarMailForm(forms.Form):
	Subject = forms.CharField(required=True)
	Content = forms.CharField(widget=forms.Textarea,required=True)

'''
{% extends "admin/app_index.html" %}
{% block content %}

<h3>Total Attendees: {{total_attendees}}</h3>
<form action="{% url 'admin:send_email' event_id=event_id %}" method='post'>  
	{% csrf_token %}
	{% for field in form %}
	<div class="form-group">
		{{field.errors}}
		{{field}}
		{{field.label_tag}}
	</div>
	{% endfor %}
	<input type="submit" value="send mail">
</form>

{% endblock %}'''
