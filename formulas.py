
def BasalMetabolicRate(gender, weight_in_kilograms, height_in_centimeters, age_in_years):
    if gender == 'Masculino':
        return (10 * weight_in_kilograms) + (6.25 * height_in_centimeters) - (5 * age_in_years) + 5
    else:
        return (10 * weight_in_kilograms) + (6.25 * height_in_centimeters) - (5 - age_in_years) - 161


def pesoIdeal(sexo, peso, estatura, edad):
    #constante para saber si es que el usuario sigue el plan recomendado
    #bajara 1.2 kilos por mes
    const = 1.2
    if sexo == 'Masculino':
        peso_ideal = (0.75 * estatura) - 62.5 
    else:
        peso_ideal = (0.75 * estatura) - 56.25
    return ((peso - peso_ideal)/ const)

