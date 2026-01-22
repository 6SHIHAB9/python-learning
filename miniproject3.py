print("Welcome to the roller coster!")
height = int(input("Enter your height: "))


if height >= 120:
    age = int(input("Please Enter your age: "))
    if age <= 12:
        fare = 5
    elif age <= 18:
        fare = 7
    elif age <= 44:
        fare = 12
    elif age >=45 and age <=55:
        fare  = 0
    if not age >=45 and age <=55:
        photo_chose = input("Enter yes if you want to take photos in the ride: ")
        if photo_chose == "yes":
            fare += 3
    print(f"Your total bill is: ${fare}")
else:
    print("You must be above 120cm to ride.")