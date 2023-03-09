def bmi(weight, height):
    bmi = (weight / (height ** 2))
    if bmi <= 18.5:
        return "Underweight"
    elif bmi > 18.6 and bmi <= 25.0:
        return "Normal"
    elif bmi > 25.1 and bmi <= 30.0:
        return "Overweight"
    elif bmi > 30:
        return "Obese"
