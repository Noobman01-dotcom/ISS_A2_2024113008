# Write Answers for part 5 here
roll_number_str = "2024113008"
digits = [int(d) for d in roll_number_str]

# e. Identify digits from your roll number that are divisible by 2, 3, and 4 and print the counts
divisible_by_2_count = len([d for d in digits if d % 2 == 0])
divisible_by_3_count = len([d for d in digits if d % 3 == 0])
divisible_by_4_count = len([d for d in digits if d % 4 == 0])

print(f"Count of digits divisible by 2: {divisible_by_2_count}")
print(f"Count of digits divisible by 3: {divisible_by_3_count}")
print(f"Count of digits divisible by 4: {divisible_by_4_count}")