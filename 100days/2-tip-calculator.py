print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
perc = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_bill += (total_bill * perc) / 100
each_person = total_bill / people
each_person = round(each_person, 2)
each_person = "{:.2f}".format(each_person)
print(f"Each person should pay: ${each_person}")