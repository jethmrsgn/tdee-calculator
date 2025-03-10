from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CalculatorTdee

# Create your views here.
def calculate_tdee(gender:str, age:int, weight:float, height:float, activity_level:str, body_fat:float):
	"""
    Calculate the Total Daily Energy Expenditure (TDEE) based on the Mifflin-St Jeor Equation.

    Parameters:
    gender (str): The gender of the individual ('male' or 'female').
    age (int): The age of the individual in years.
    weight (float): The weight of the individual in kilograms.
    height (float): The height of the individual in centimeters.
    activity_level (str): A multiplier representing the individual's activity level.
    body_fat (float): Percentage of body fat.

    Returns:
    float: The estimated daily caloric expenditure.
    """

	tdee = ((10 * weight + 6.25 * height - 5 * age) + (5 if gender == 'male' else -151)) * float(activity_level)
	return tdee


def index(request):
	""" Handle the TDEE calculator form submission and render the index page."""

	if request.method == 'POST':
		form = CalculatorTdee(request.POST)
		if form.is_valid():
			gender = form.cleaned_data['gender']
			age = form.cleaned_data['age']
			weight = form.cleaned_data['weight']
			height = form.cleaned_data['height']
			activity_level = form.cleaned_data['activity_level']
			tdee = calculate_tdee(gender=gender,age=age,weight=weight,height=height,activity_level=activity_level,body_fat=None)
			messages.success(request,tdee)
			return redirect('result')
		# render(request,'calculator/index.html',{'tdee':tdee})
	else:
		form = CalculatorTdee()

	context = {'form': form}
	return render(request,'calculator/index.html', context)

def result(request):
	return render(request,'calculator/result.html')