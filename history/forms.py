from django import forms

class GetUser(forms.Form):
	username = forms.CharField(max_length=50)
