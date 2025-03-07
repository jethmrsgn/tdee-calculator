from django import forms

class CalculatorTdee(forms.Form):
	gender = forms.CharField(max_length=20,required=True)
