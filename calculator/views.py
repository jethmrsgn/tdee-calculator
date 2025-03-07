from django.shortcuts import render, redirect
from .forms import CalculatorTdee

# Create your views here.
def calculate_tdee(gender:str, age:int, weight:float, height:float, activity_level:str, body_fat:float):
	tdee = ((10 * weight + 6.25 * height - 5 * age) + (5 if gender == 'male' else -151)) * float(activity_level)
	return tdee

def index(request):
	if request.method == 'POST':
		form = CalculatorTdee(request.POST)
		if form.is_valid():
			gender = form.cleaned_data['gender']
			age = form.cleaned_data['age']
			weight = form.cleaned_data['weight']
			height = form.cleaned_data['height']
			activity_level = form.cleaned_data['activity_level']
			tdee = calculate_tdee(gender=gender,age=age,weight=weight,height=height,activity_level=activity_level,body_fat=None)
			return render(request,'calculator/index.html',{'tdee':tdee})
	else:
		form = CalculatorTdee()

	context = {'form': form}
	return render(request,'calculator/index.html', context)