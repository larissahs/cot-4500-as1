# imported libraries
from numpy import *
from decimal import Decimal

# function to convert mantissa string to an int
def convert_matissa_to_int(mantissa_str):
    mantissa_int = 0
    # go through mantissa
    for i in range(len(mantissa_str)):
        mantissa_int += int(mantissa_str[i]) * pow(1/2, i+1)
     
    return (mantissa_int)

# function to find absolute error: |p - p*|
def get_absolute_error(value:float, rounded: float):
    return abs(value - rounded)

# function to find relative error: |p - p*| / |p|
def get_relative_error(value:float, rounded: float):
    value = Decimal(value)
    rounded = Decimal(rounded)
    absolute_err = get_absolute_error(value, rounded)

    return (absolute_err / value)


def check_for_negative_1_exponent_term(function: str) -> bool:
    if "-1**k" in function:
        return True

    return False

# pre requisite for question 5
def check_for_alternating(function: str):
    term_check = check_for_negative_1_exponent_term(function)

    return term_check

# pre requisite for question 5
def check_for_decreasing(function: str, x: int):
    decreasing_check = True
    k = 1
    starting_val = abs(eval(function))

    for k in range(2, 100):
        result = abs(eval(function))
        if starting_val <= result:
            decreasing_check = False

    return decreasing_check

def get_minimum_term_function():
    error_tolerance = .0001
    k = 1
    flag = True

    while flag == True:
        func = (-1**k) * (x**k) / (k**3)
        if abs(func) < error_tolerance:
            flag = False
            break
        k += 1

    print(k-1)


def bisection_method(left: float, right: float, function: str):
    # pre requisites (opposite ranges)
    x = left
    intial_left = eval(function)
    x = right
    intial_right = eval(function)
    if intial_left * intial_right >= 0:   
        return

    tolerance: float = .0001
    diff: float = right - left
    iteration_counter = 0

    while (diff >= tolerance and iteration_counter <= 20):
        iteration_counter += 1

        # get the mindpoint
        mid_point = (left + right) / 2
        x = mid_point
        evaluated_midpoint = eval(function)

        if evaluated_midpoint == 0.0:
            break
        
        # get the left
        x = left
        evaluated_left_point = eval(function)
        
        # check if we have crossed the origin point: f(midpoint) * f(left_point) changed signs
        first_conditional: bool = evaluated_left_point < 0 and evaluated_midpoint > 0
        second_conditional: bool = evaluated_left_point > 0 and evaluated_midpoint < 0

        if first_conditional or second_conditional:
            right = mid_point
        else:
            left = mid_point
        
        diff = abs(right - left)

    print("\r")
    print(iteration_counter)

def custom_derivative(value):
    return (3 * value* value) - (2 * value)

def newton_raphson(initial_approximation: float, tolerance: float, sequence: str):
    iteration_counter = 0

    #x = initial_approximation

    # approximation f / f'
    approximation: float = eval(sequence) / custom_derivative(initial_approximation)

    while(abs(approximation) >= tolerance):
        x = initial_approximation
        
        # approximation f / f'
        approximation: float = eval(sequence) / custom_derivative(initial_approximation)
        initial_approximation -= approximation
        iteration_counter += 1
    
    print("\r")
    print(iteration_counter)

if __name__ == "__main__":

    # Question 1
    bits_64 = '0100000001111110101110010000000000000000000000000000000000000000'
    sign = int(bits_64[0])
    exponent = int(bits_64[1 : 12], 2)
    exponent = exponent - 1023
    mantissa_str = bits_64[12 : ]
    mantissa_int = convert_matissa_to_int(mantissa_str)
    value_question1 = pow(-1, sign) * pow(2, exponent) * (mantissa_int + 1)
    print(value_question1)
 
    # Question 2: three-digit chopping arithmetic
    chopped_answer = int(value_question1)
    print('\r')
    print("{:.1f}".format(chopped_answer))

    # Question 3: three-digit rounding arithmetic
    rounded_answer = round(value_question1)
    print("\r")
    print("{:.1f}".format(rounded_answer))

    # Question 4: absolute error with value from Q1 and Q3
    absolute_err = get_absolute_error(value_question1, rounded_answer)
    print("\r")
    print("{:.4f}".format(absolute_err))

    # Question 4: relative error with value from Q1 and Q3
    relative_err = get_relative_error(value_question1, rounded_answer)
    print("{:.31f}".format(relative_err))
    
    # Question 5
    x: int = 1
    function_question5: str = "(-1**k) * (x**k) / (k**3)"
    # check pre requisites
    check1: bool = check_for_alternating(function_question5)
    check2: bool = check_for_decreasing(function_question5, x)
    print("\r")
    # if both conditons are met then we can go ahead and perform calculations
    if check1 and check2:
        get_minimum_term_function()

    # Question 6: Bisection Method
    left = -4
    right = 7
    function_question6 = "x**3 + (4*(x**2)) - 10"
    bisection_method(left, right, function_question6)

    # Question 6: Newton Raphson Method
    initial_approximation: float = -4.0
    tolerance: float = .0001
    sequence: str = "x**3 - (x**2) + 2"
    #sequence: str = "x**3 + (4*(x**2)) - 10"
    newton_raphson(initial_approximation, tolerance, sequence)
    print("\r")

    





    

