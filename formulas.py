
def BasalMetabolicRate(gender, weight_in_kilograms, height_in_centimeters, age_in_years):
    if gender == 'Masculino':
        return (10 * weight_in_kilograms) + (6.25 * height_in_centimeters) - (5 * age_in_years) + 5
    else:
        return (10 * weight_in_kilograms) + (6.25 * height_in_centimeters) - (5 - age_in_years) - 161

