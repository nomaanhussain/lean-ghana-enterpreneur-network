from allauth.account.adapter import DefaultAccountAdapter 
from django.forms import ValidationError 

class UsernameMaxAdapter(DefaultAccountAdapter): 
	def clean_username(self, username, shallow=None): 
		print("aaaa",type(len(username)))
		if len(username) > 30: 
			raise ValidationError('Please enter a username value less than the current one') 
		
		# For other default validations. 
		return DefaultAccountAdapter.clean_username(self, username) 
