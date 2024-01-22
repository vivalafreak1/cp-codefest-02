def ganjil(m):
    # Ensure the input is within the constraint
    if 1 <= m <= 100:
        odd_numbers = [num for num in range(1, m+1) if num % 2 != 0]
        return odd_numbers
    else:
        return []

# Get user input for M
try:
    m_value = int(input("Enter a value for M (1 <= M <= 100): "))
    result = ganjil(m_value)

    if result:
        print(f"Odd numbers within the range (1 <= M <= 100): {result}")
    else:
        print("Invalid input for M. Please enter a value within the specified constraint.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
