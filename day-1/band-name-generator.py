WELCOME_MESSAGE = "Welcome to the band name generator"
CITY_NAME_PROMPT_MSG = "Please, introduce your city's name\n"
PET_NAME_PROMPT_MSG = "Now, introduce your pet's name\n"

print(WELCOME_MESSAGE)
city_name = input(CITY_NAME_PROMPT_MSG)
pet_name = input(PET_NAME_PROMPT_MSG)

print(f"Your automatically-generated band name is: {str(city_name)} {str(pet_name)}")