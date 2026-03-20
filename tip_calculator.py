import sys

print("Welcome to split calculator")

total_bill = float(sys.argv[1])
percentage = int(sys.argv[2])
split = int(sys.argv[3])

pay = (total_bill / split) * (1 + (percentage / 100))
pay1 = round(pay, 2)

print(f"Each person should pay: ${pay1}")
