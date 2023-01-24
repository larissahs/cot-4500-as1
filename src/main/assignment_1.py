# imported libraries
from numpy import *

def convertToInt(mantissa_str):
    power_count = -1
    mantissa_int = 0
 
    # go through mantissa
    for i in mantissa_str:
        mantissa_int += (int(i) * pow(2, power_count))
        power_count -= 1
         
    return (mantissa_int + 1)

# function to find absolute error
# |p - p*|
def absolute_error(precise:float, approximate: float):

    sub_operation = precise - approximate

    return abs(sub_operation)

# function to find relative error
# |p - p*| / |p|
def relative_error(precise:float, approximate: float):

    sub_operation = absolute_error(precise, approximate)
    div_operation = sub_operation / precise

    return div_operation

# # pre requisite
# def check_for_alternating(function_we_got: str):
#     term_check = check_for_negative_1_exponent_term(function_we_got)

#     return term_check

# def check_for_negative_1_exponent_term(function: str) -> bool:
#     if "-1**k" in function:
#         return True

#     return False

# # pre requisite
# # def check_for_decreasing(function_we_got: str, x: int):
# #     decreasing_check = True
# #     k = 1
# #     starting_val = abs(eval(function_we_got))
# #     for k in range(2, clea):
# #         result = abs(eval(function_we_got))

# #         print(result)
# #         if starting_val <= result:
# #             decreasing_check = False

# #     return decreasing_check


if __name__ == "__main__":

    # x: double = double(int('0100000001111110101110010000000000000000000000000000000000000000',2))
    # print("{:.5f}".format(x))
    ieee_64 = '0|10000000|1111110101110010000000000000000000000000000000000000000'
    sign = int(ieee_64[0])
    exponent = int(ieee_64[2 : 10], 2)
    exponent = exponent - 127
    mantissa_str = ieee_64[11 : ]
    mantissa_int = convertToInt(mantissa_str)
    real_no = pow(-1, sign) * mantissa_int * pow(2, exponent)
    #print(real_no)
    print("{:.5f}".format(real_no))
 
    # get three-digit chopping arithmetic
    # chopping = real_no
    # chopping /= 10.
    print("\n")
    print("{:.2f}".format(real_no))

    #get three-digit rounding arithmetic
    print(round(real_no, 3))

    # print absolute error
    absolute = absolute_error(real_no, round(real_no, 3))
    print("\n")
    print("%f" % absolute)
    # print relative error
    relative = relative_error(real_no, round(real_no, 3))
    print("%f" % relative)
    

    # check pre requisites
    # function_a: str = "(-1**k) * (x**k) / (k**3)"
    # x: int = 1
    # check1: bool = check_for_alternating(function_a)
    # check2: bool = check_for_decreasing(function_a, x)

    # print(check1 and check2)

    # if check1 and check2:
    #     use_minimum_term_function(function_a)
    

    





    

