# This is a program that calculates the sales tax
cost = float(input("Enter the cost of the item: "))

# We are going to calculate the tax rate of 6.5%
sales_tax = (cost * .065)

print(f"the sales tax is: ${sales_tax:.2f}")

total_cost = (cost + sales_tax)
print(f"the total cost is ${total_cost:.2f}")