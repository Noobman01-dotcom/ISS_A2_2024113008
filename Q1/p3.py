# Write Answers for part 3 here
roll_number_str = "2024113008"
digits = [int(d) for d in roll_number_str]


# c. Identify even number digits
even_digits = [d for d in digits if d % 2 == 0]
print(f"Even number digits: {even_digits}")