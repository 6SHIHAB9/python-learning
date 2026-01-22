print("Welcome to Python Pizza Deliveries")

size = input("What size pizza do you want? S, M or L: ")
pepparoni = input("Do you want pepparoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese on your pizza? Y or N: ")

fare = 0
if size == "S":
    fare += 15
    if pepparoni == "Y":
        fare += 2
    if extra_cheese == "Y":
        fare += 1
elif size == "M":
    fare += 20
    if pepparoni == "Y":
        fare += 3
    if extra_cheese == "Y":
        fare += 1
elif size == "L":
    fare += 25
    if pepparoni == "Y":
        fare += 3
    if extra_cheese == "Y":
        fare += 1


print(f"Your final bill is ${fare}")

