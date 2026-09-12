# Ask the user for their name and greet them
name = input("What is your name? ")
print(f"Hello, {name}! Let's count some numbers.")

# Ask the user how high they want to count
# We use int() to convert the text input to a whole number
max_number = int(input("Enter a number to count up to: "))

# Use a loop to print the numbers sequentially
print("\nCounting:")
for i in range(1, max_number + 1):
    print(i)

print("All done!")