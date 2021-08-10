# Day 2
print("Welcome to the Tip Calculator")

total_bill = input("What was the total bill?: £")
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15?: "))
# percent = (percentage_tip/100) + 1
people = int(input("How many people to split the bill?: "))

distribution = (float(total_bill) / people) * (percentage_tip / 100) + 1
rounded_dist = "{:.2f}".format(distribution)
print(f"Each person pays: £{rounded_dist}")
