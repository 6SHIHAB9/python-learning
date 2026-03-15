print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many peoplr to split the bill? "))
 

bill_with_tip = total_bill + total_bill/100*tip
each_persons_bill = round(bill_with_tip/people, 2)


print(f"Each person should pay: ${each_persons_bill}")

