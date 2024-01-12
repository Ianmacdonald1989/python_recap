# # #function 
# print("a value")
# print(input("ask for a value "))

# #methods -> functions of datatypes
# print("value".upper())
# print("VALUE".lower())
# print("value".replace("e", "3"))


# # #new functions 
# print(abs(-1))
# print(max(10,5))
# print(min(0,1))
# print(len("test"))

# #exercise pythagoras theory

# side_a = int(input("The width of the triangle: "))
# side_b = int(input("The height of the triangle: " ))
# hypotenuse = (side_a ** 2 + pow(side_b, 2)) ** (1/2)
# print(" the hypotenuse is: ", round(hypotenuse, 2))

#while loops
def print_x_times(parameter, loop_amount = 5):
    counter = 0
    print(global_var)
    while counter < loop_amount:
        print(counter, parameter)
        counter += 1
    return 'something else'
#
def hypotenuse_calculator(side_a = 1, side_b = 1):
    hypotenuse = (side_a ** 2 + side_b ** 2) ** (1/2)
    return round(hypotenuse, 2)

def shout(output_string = 'hello', repitition_amount = 2):
    if repitition_amount <= 10:
        for i in range(repitition_amount):
            print(output_string.upper())
        else:
            print('you are too loud')
        return 'done'

# call
# print('print')
# global_var = 'global variable'
# test = print_x_times('test', 4)
# print(test)

print(hypotenuse_calculator(1, 1))


#exercise
status = shout()
print(status)




