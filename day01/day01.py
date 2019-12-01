import math

sum1 = 0
sum2 = 0

def calcFuel(mass):
    mass = int(mass)
    return math.floor(mass / 3) - 2

with open('input.txt') as f:
    for mass in f.readlines():
        fuel = calcFuel(mass)
        sum1 += fuel

        sum2 += fuel
        while fuel > 0:
            fuel = calcFuel(fuel)
            if(fuel > 0):
                sum2 += fuel

print("Sum1 : " + str(sum1))
print("Sum2 : " + str(sum2))
