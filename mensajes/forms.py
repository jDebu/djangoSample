from django import forms
from .services import Services

'''
class DniForm(forms.Form):
	DNI = forms.CharField()
	def load_data(self):
		service_dni=Services()
		#data=service_dni.get_data_dni(self.fields['DNI'])
		#return data
		
class NameForm(forms.Form):
	Nombres = forms.CharField()
	Apellidos = forms.CharField()
'''

class ContactForm(forms.Form):
    name = forms.CharField(max_length=60)
    message = forms.CharField(max_length=200, widget=forms.TextInput)


class SubscriptionForm(forms.Form):
    email = forms.EmailField()
    want_spam = forms.BooleanField(required=False)


class SuggestionForm(forms.Form):
    text = forms.CharField(max_length=200, widget=forms.TextInput)
    type = forms.ChoiceField(choices=[('bug', 'Bug'), ('feature', 'Feature')])


class DniForm(forms.Form):
	dni = forms.CharField(max_length=60, widget=forms.TextInput,label='DNI')

class NameForm(forms.Form):
	dni_ = forms.CharField(max_length=60, widget=forms.TextInput)
	names = forms.CharField(max_length=200,widget=forms.TextInput,label='Nombres')
	last_names = forms.CharField(max_length=200,widget=forms.TextInput,label='Apellidos')