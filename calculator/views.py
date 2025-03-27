from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CalculatorTdee
from history.models import UserHistory,ActivityLevel
import json

from math import ceil

# Business functionalities.
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

def calculate_macros(maintenance_calories):
    """Calculate macronutrients base on carb plan"""
    calorie_adjustment = {
		'maintenance': 0,
        'cutting': -500,
        'bulking': 500
	}
    macro_ratios = {
        "moderate_carb": (0.30, 0.35, 0.35),
        "lower_carb": (0.40, 0.40, 0.20),
        "higher_carb": (0.30, 0.20, 0.50),
    }

    calories_per_gram = {"protein": 4, "fats": 9, "carbs": 4}

    results = {}

    for adjustment_type, adjustment in calorie_adjustment.items():
        calories = maintenance_calories + adjustment
        results[adjustment_type] = {}
        for plan, (protein_ratio, fat_ratio, carb_ratio) in macro_ratios.items():
            protein_calories = calories * protein_ratio
            fat_calories = calories * fat_ratio
            carb_calories = calories * carb_ratio

            protein_grams = protein_calories / calories_per_gram["protein"]
            fat_grams = fat_calories / calories_per_gram["fats"]
            carb_grams = carb_calories / calories_per_gram["carbs"]

            results[adjustment_type][plan] = {
				"calories": ceil(calories),
				"protein": round(protein_grams, 2),
				"fats": round(fat_grams, 2),
				"carbs": round(carb_grams, 2),
			}
    return results

# Views here
def index(request):
	""" Handle the TDEE calculator form submission and render the index page."""

	if request.method == 'POST':
		form = CalculatorTdee(request.POST)
		if form.is_valid():
			username= form.cleaned_data['user']
			gender = form.cleaned_data['gender']
			age = form.cleaned_data['age']
			weight = form.cleaned_data['weight']
			height = form.cleaned_data['height']
			activity_level = form.cleaned_data['activity_level']
			tdee = calculate_tdee(gender=gender,age=age,weight=weight,height=height,activity_level=activity_level,body_fat=None)

			initial_form = {
				'gender':gender,
				'age':age,
				'weight':weight,
				'height':height,
				'activity_level':activity_level
			}
			request.session['tdee'] = ceil(tdee)
			request.session['initial_form']= json.dumps(initial_form)

			messages.success(request, f'Your TDEE is {tdee} kcal/day')
			macros = calculate_macros(ceil(tdee))

			if not (username == ""):

				macros_in_json = json.dumps(macros)

				UserHistory.objects.create(
					user = username,
					gender = gender,
					age = age,
					weight = weight,
					height = height,
					activity_level = ActivityLevel.objects.get(value=activity_level),
					macros = macros_in_json
				)
			selected_macros = macros['maintenance']
			context = {
				'form': form,
				'tdee':ceil(tdee),
				'macros':selected_macros,
				'active_tab':'maintenance'
				}
			return render(request,'calculator/index.html', context)
	else:
		form = CalculatorTdee()

	context = {'form': form}
	return render(request,'calculator/index.html', context)

def result(request,plan='maintenance',current_tdee=0):
	""" Handles the visualization of the result of TDEE and macronutrients"""
	tdee = request.session.pop('tdee',0)
	initial_dict = json.loads(request.session.pop('initial_form'))

	final_tdee = tdee if current_tdee is None or current_tdee == 0 else current_tdee
	macros = calculate_macros(final_tdee)
	selected_macros = macros[plan]
	form = CalculatorTdee(initial= initial_dict)

	request.session['initial_form']= json.dumps(initial_dict)	
	print(initial_dict)

	return render(request,'calculator/index.html',{
		'tdee':final_tdee,
		'macros':selected_macros,
		'active_tab':plan,
		'form': form
	})

