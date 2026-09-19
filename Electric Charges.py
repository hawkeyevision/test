# calculating electric bill
#KW represents kilowatt hours.

#prompting for kilowatt hours
KW = float(input("Please enter a number greater then zero for the kilowatt hours consumed: "))

print(f"you entered {KW:.2f} kilowatt hours")

#We are evaluating the rate to be charged
if KW <= 1000:
    amount = (KW * 7.8633)
    print(f"the monthly electric bill is: {amount:.2f} dollars")
elif KW > 1000:
    amount = (KW * 9.259)
    print(f"the monthly electric bill is: {KW:.2f} dollars")
else:
    print("Error")
