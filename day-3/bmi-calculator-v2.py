WELCOME_MESSAGE = "Welcome to the BMI calculator"
WEIGHT_PROMPT_MSG = "Please, introduce your weigth in Kilograms\n"
HEIGHT_PROMPT_MSG = "Please, introduce your heigth in Meters\n"

print(WELCOME_MESSAGE)
weight = float(input(WEIGHT_PROMPT_MSG))
height = float(input(HEIGHT_PROMPT_MSG))

bmi = round(weight / (height**2), 1)

if bmi < 18.5:
    bmi_result_message = "You are underweight"
elif bmi < 25:
    bmi_result_message = "You have a normal weight"
elif bmi < 30:
    bmi_result_message = "You are overweight"
elif bmi < 35:
    bmi_result_message = "You are obese"
else:
    bmi_result_message = "You are clinically obese"

print(f"Your BMI is: {bmi}, {bmi_result_message}")
