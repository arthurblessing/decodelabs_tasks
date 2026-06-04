total = 0  # Accumulator initialized OUTSIDE the loop

while True:
    entry = input("Enter expense (or 'quit' to finish): ")
    
    if entry == "quit":
        break  # Kill switch
    
    try:
        expense = int(entry)  # Gatekeeper: string → integer
        total += expense      # Accumulator pattern
        print(f"Added. Running total: {total}")
    except ValueError:
        print("Invalid input. Enter a number.")

print(f"\nFinal Total Spent: {total}")
