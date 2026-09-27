##############################################################################################
# This is my circle function
# r = a variable to hold the value of the user specified radius
# Pi = a constant defined as 3.14159
# A = variable to hold teh calculated area of the circle

def calc_area_circle():
    Pi = 3.14159
    r = input("Enter the radius of the circle: ")
    r = float(r)
    A = Pi * (r ** 2)
    #rounding the calculated value of area to 2 decimal places
    A = f"{A: .2f}"
    return A

A = calc_area_circle()
print(f"The area of the circle is: {A}")

##############################################################################################
# This is my taxes function
# The variable amount is used to hold the imputed value for amount that needs to be taxed
# The variable final_amount is used to hold the calculated amount after including tax
# TAX_RATE is a constant that's been assigned the fixed value of 0.065 for a tax rate of 6.5%
amount = float(input("Enter the money amount in USD: "))
# setting up function and passing the value of amount of imputed amount to it
def total_amt_due(amount):
    TAX_RATE = 0.065
    totalamt = amount + (amount * TAX_RATE)
    return totalamt

final_amount = total_amt_due(amount)
print(f"The amount due is: ${final_amount:.2f}")

##############################################################################################
# This is my temperature function
# temp_fahrenheit is a variable that accepts the user input(temp in fahrenheit)
# temp_fahrenheit is the parameter that is passed to the function
# local variable temp_celsius holds and returns this value
# converted_temp holds the value returned from the function
temp_fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
#print(f"You entered: {temp_fahrenheit:.1f} F")

def convert_to_celsius(temp_fahrenheit):
    temp_celsius = (temp_fahrenheit - 32) * (5 / 9)
    return temp_celsius

converted_temp = convert_to_celsius(temp_fahrenheit)
print(f"The temperature in celsius is: {converted_temp:.1f} C")