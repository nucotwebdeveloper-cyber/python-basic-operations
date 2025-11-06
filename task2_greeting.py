# Task 2: Create a Personalized Greeting

# Step 1: Take first and last name
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

# Step 2: Concatenate to make full name
full_name = first_name + " " + last_name

# Step 3: Print greeting
print(f"\nHello, {full_name}! Welcome to Python programming.")
