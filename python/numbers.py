import random
import time

number=0

print("Setup:")

print("Randomness:")
add_chance=int(input("Chance to add: "))
subtract_chance=int(input("Chance to subtract: "))
multiply_chance=int(input("Chance to multiply: "))
divide_chance=int(input("Chance to divide: "))

rand_range=add_chance+subtract_chance+multiply_chance+divide_chance

print("Range:")
add_min=int(input("Minimum to add: "))
add_max=int(input("Maximum to add: "))
subtract_min=int(input("Minimum to subtract: "))
subtract_max=int(input("Maximum to subtract: "))
multiply_min=int(input("Minimum to multiply: "))
multiply_max=int(input("Maximum to multiply: "))
divide_min=int(input("Minimum to divide: "))
divide_max=int(input("Maximum to divide: "))

wait=int(input("How long to wait between numbers: "))

while True:
    rng=random.randint(1, rand_range)

    if 1<=rng<=add_chance:
        number+=random.randint(add_min, add_max)
    elif add_chance<rng<=add_chance+subtract_chance:
        number-=random.randint(subtract_min, subtract_max)
    elif add_chance+subtract_chance<rng<=add_chance+subtract_chance+multiply_chance:
        number*=random.randint(multiply_min, multiply_max)
    elif add_chance+subtract_chance+multiply_chance<rng<=add_chance+subtract_chance+multiply_chance+divide_chance:
        number/=random.randint(divide_min, divide_max)

    print(number)
    time.sleep(wait)
