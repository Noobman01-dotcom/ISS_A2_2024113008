# Write Answers for part 4 here
roll_number_str = "2024113008"
digits = [int(d) for d in roll_number_str]

# d. Identify “zeros” from your roll number and print the count
zero_count = digits.count(0)
print(f"Count of zeros: {zero_count}")
