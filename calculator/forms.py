from django import forms

ACTIVITY_LEVEL = (
	(1.2, 'Sedentary (little to no exercise)'),
	(1.375, 'Lightly active (light exercise/sports 1-3 days a week)'),
	(1.55, 'Moderately active (moderate exercise 3-5 days a week)'),
	(1.725, 'Very active (hard exercise 6-7 days a week)'),
	(1.9, 'Super active (very hard exercise, physical job, or training twice a day)'),
)

class CalculatorTdee(forms.Form):
	gender = forms.ChoiceField(widget=forms.RadioSelect,
							choices=[('Male','Male'),('Female','Female')],)
	age = forms.IntegerField(min_value=0,widget=forms.NumberInput(
		attrs={'step':'any'}))
	weight = forms.FloatField(min_value=0,widget=forms.NumberInput(
		attrs={'placeholder':'kg','step':'any'}))
	height = forms.FloatField(min_value=0,widget=forms.NumberInput(
		attrs={'placeholder':'cm','step':'any'}))
	activity_level = forms.ChoiceField(choices=ACTIVITY_LEVEL)
