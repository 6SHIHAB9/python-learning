alph = [
  'A','B','C','D','E','F','G','H','I','J','K','L','M',
  'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
  'a','b','c','d','e','f','g','h','i','j','k','l','m',
  'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

num = [
  '0','1','2','3','4','5','6','7','8','9'
]

sym = [
  '!','@','#','$','%','^','&','*',
  '(',')','-','_','=','+',
  '[',']','{','}','|','\\',
  ':',';','"',"'",'<','>','?',
  ',','.','/','~','`'
]


print("Welcome to the Password Generator!")
alphabets = int(input("How many alphabets would you like?"))
numbers = int(input("How many numbers would you like?"))
symbols = int(input("How many symbols would you like?"))

import random

place_holder = ""
for i in range(alphabets):
    place_holder =  place_holder + random.choice(alph)   
for i in range(numbers):
    place_holder = place_holder + random.choice(num)
for i in range(numbers):
    place_holder = place_holder + random.choice(sym)

list = list(place_holder)
random.shuffle(list)

password = ""
for i in list:
    password += i

print(password)


