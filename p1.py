roll_number_str = "2024113008"
digits = [int(d) for d in roll_number_str]

# a. Identify prime number digits
prime_digits = [d for d in digits if d in [2, 3, 5, 7]]
print(f"Prime number digits: {prime_digits}")