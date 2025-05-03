roll_number_str = "2024113008"
digits = [int(d) for d in roll_number_str]

# b. Identify odd number digits
odd_digits = [d for d in digits if d % 2 != 0]
print(f"Odd number digits: {odd_digits}")
