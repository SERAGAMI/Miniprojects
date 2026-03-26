import random
a=0
random_number = random.randint(1, 5)
while a != random_number:
    a = int(input("Enter your number:"))
    if a > random_number:
     print("Number is smaller")
    elif a < random_number:
     print("Number is larger")
print("Congrats!!! You guessed the number.")