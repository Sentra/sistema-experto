import random

from kanren import *
import pandas as pd

dataset_url = 'https://raw.githubusercontent.com/Sentra/lobueno/master/foods.csv'
data = pd.read_csv(dataset_url, error_bad_lines=False)

meals = data['Food'].values
calories = data['Calories'].values
categories = data['Type'].values

dish_calories = Relation()
dish_category = Relation()

for i in range(len(meals)):
    fact(dish_calories, meals[i], calories[i])
    fact(dish_category, meals[i], categories[i])


def three_meals_fit_requirements(breakfast, food_calories_breakfast, lunch, food_calories_lunch, dinner,
                                 food_calories_dinner):
    result = conde((
        dish_category(breakfast, "Breakfast"),
        dish_category(lunch, "Lunch"),
        dish_category(dinner, "Dinner"),
        dish_calories(breakfast, food_calories_breakfast),
        dish_calories(lunch, food_calories_lunch),
        dish_calories(dinner, food_calories_dinner))
    )
    return result


def generate_dishes(number_of_dishes, BMR):
    breakfast_option, breakfast_calories, lunch_option, lunch_calories, dinner_options, dinner_calories = vars(6)
    solutions = run(1000, [[breakfast_option, breakfast_calories], [lunch_option, lunch_calories],
                        [dinner_options, dinner_calories]],
                    (three_meals_fit_requirements(breakfast_option, breakfast_calories, lunch_option, lunch_calories,
                                                  dinner_options, dinner_calories)))

    solutions_list = [item for item in solutions]
    random.shuffle(solutions_list)
    counter = 0
    solutions_matching_bmr = []
    for solution in solutions_list:
        if counter == number_of_dishes:
            break
        breakfast = int(solution[0][1])
        lunch = int(solution[1][1])
        dinner = int(solution[2][1])
        minimum = BMR - 400
        total_calories = breakfast + lunch + dinner
        if total_calories < BMR and (total_calories > minimum):
            new_solution = ([solution[0][0], solution[1][0], solution[2][0]], total_calories)
            solutions_matching_bmr.append(new_solution)
            counter += 1

    return solutions_matching_bmr
