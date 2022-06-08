OPERATION_PROMPT_MSG = lambda text : f"Choose one of these operations: {text}\n"
CONTINUE_PROMPT_MSG = "Do you want to continue calculating? (y/n)\n"
INPUT_1_PROMPT_MSG = "Please, enter a number\n"
INPUT_2_PROMPT_MSG = "Please, enter another number\n"

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def pick_operation():
    operation_chosen = None
    prompt = ''.join([(operation + ' ') for operation in operations])
    print("Please, select the operation to apply")
    while (not operation_chosen in operations):
        operation_chosen = input(OPERATION_PROMPT_MSG(prompt))
        if (operation_chosen in operations):
            return operations[operation_chosen]
        print('Please, make sure of selecting one of the valid options')

def calculate():
    first_calculation = True
    keep_calculating = True
    total = 0
    while keep_calculating:
        if first_calculation:
            input_1 = float(input(INPUT_1_PROMPT_MSG)) # First operation / operation after clearing
            first_calculation = False
        else:
            input_1 = total
        op = pick_operation()
        input_2 = float(input(INPUT_2_PROMPT_MSG))
        
        total = op(input_1, input_2)
        print(f"Your total calculation is: {total}")
        if input(CONTINUE_PROMPT_MSG) == 'n':
            keep_calculating = False
    
# REALLY GOOD APPROACH TO HAVING TO "PICK" BETWEEN DIFFERENT FUNCTIONS TO BE EXECUTED, BASED ON INPUT, INSTEAD OF A SWITCH-CASE APPROACH: 1. Associate the "input-to-be" as a key to "select" the function (Use a Map); 2. validate through a conditional that the inputted value is among those keys to continue the operation
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

calculate()





