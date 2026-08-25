print("--- Welcome to the Python Calculator ---")

while True:
    # 1. Ask the user what action they want to take
    print("\nChoose an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")
    
    choice = int(input("Enter choice (1-5): "))

    # Check if the user wants to leave the program (No quotes around 5)
    if choice == 5:
        print("Goodbye!")
        break  # This exits the while loop immediately

    # 2. Ask for numbers INSIDE the loop (indented by 4 spaces)
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # 3. Perform the calculation based on the choice (No quotes around 1, 2, 3, 4)
    if choice == 1:
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
            
    elif choice == 2:
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
            
    elif choice == 3:
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
            
    elif choice == 4:
        # Check for division by zero to prevent a crash
        if num2 == 0:
            print("Error! You cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Invalid input! Please choose a number from (2-5)")