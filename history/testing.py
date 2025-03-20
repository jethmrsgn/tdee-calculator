from math import ceil
import json
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

macros = calculate_macros(2400)
json_object = json.dumps(macros)
print(json_object)