from kanren import *
import pandas as pd

dataset_url = 'https://raw.githubusercontent.com/zaj-e/lobueno/master/foods.csv'
data = pd.read_csv(dataset_url, error_bad_lines=False)

meals = data['Food'].values
calories = data['Calories'].values
categories = data['Type'].values

dish_calories = Relation()
dish_category = Relation()

for i in range(len(meals)):
    fact(dish_calories, meals[i], calories[i])
    fact(dish_category, meals[i], categories[i])


def three_meals_fit_requirements(breakfast, food_calories_breakfast, lunch, food_calories_lunch):
    result = conde((
        dish_category(breakfast, "Breakfast"),
        dish_category(lunch, "FullMeal"),
        dish_calories(breakfast, food_calories_breakfast),
        dish_calories(lunch, food_calories_lunch),)
    )
    return result


def generate_dishes(number_of_dishes, BMR):
    breakfast_option, breakfast_calories, lunch_option, lunch_calories = vars(4)
    solutions = run(number_of_dishes, [[breakfast_option, breakfast_calories], [lunch_option, lunch_calories]],
                    (three_meals_fit_requirements(breakfast_option, breakfast_calories, lunch_option, lunch_calories)))

    solutions_matching_bmi = [([solution[0][0], solution[1][0], solution[1][0]], total_calories)
                              for solution in solutions if
                              (total_calories := int(solution[0][1]) + (2 * int(solution[1][1]))) < BMR and (total_calories > BMR - 400)]

    if len(solutions_matching_bmi) < number_of_dishes:
        redundant_solution = [solutions_matching_bmi[0] for _ in range(number_of_dishes)]
        return redundant_solution

    return solutions_matching_bmi