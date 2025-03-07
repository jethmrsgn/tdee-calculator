from django.shortcuts import render



ACTIVITY_LEVEL = {
	'sedentary': 1.2,
	'lightly':1.375,
	'moderate':1.725,
	'very':1.9
}
# Create your views here.
def calculate_tdee(gender:str, age:int, weight:float, height:float, activity_level:str, body_fat:float):
	act_level = activity_level.split()[0].lower()
	tdee = ((10 * weight + 6.25 * height - 5 * age) + (5 if gender == 'male' else -151)) * ACTIVITY_LEVEL[act_level]
	return tdee

def index(request):
	return render(request,'calculator/index.html',{
		'tdee':calculate_tdee(gender='male',age=28,weight=87,height=169,activity_level='Moderate active',body_fat=None)
	})
