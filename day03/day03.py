import math

def handleCoordinate(init, system, crossings, x, y, steps):
    if init and (x,y) not in system:
        system[(x, y)] = steps
    if not init and (x,y) in system and not (x,y) in crossings:
        totalSteps = system[(x, y)] + steps
        crossings[(x,y)] = totalSteps

system = {}
crossings = {}

isInitPhase = True

with open('input.txt') as file:
    for input in file.readlines():
        x = 0
        y = 0
        steps = 0

        system[(x, y)] = steps

        for move in input.split(','):
            direction = move[0]
            distance = int(move[1:])

            manipulator = None

            if direction in ('R', 'U'):
                manipulator = 1
            elif direction in ('L', 'D'):
                manipulator = -1
            else:
                raise Exception('Unknown direction ' + direction)

            if direction in ('R', 'L'):
                for i in range(1, distance + 1):
                    x = x + manipulator
                    steps = steps + 1
                    handleCoordinate(isInitPhase, system, crossings, x, y, steps)
            elif direction in ('U', 'D'):
                for i in range(1, distance + 1):
                    y = y + manipulator
                    steps = steps + 1
                    handleCoordinate(isInitPhase, system, crossings, x, y, steps)

        isInitPhase = False


print("Crossings: " + str(len(crossings)))
nearest = None
leastSteps = None

for crossing in crossings:
    x = crossing[0]
    y = crossing[1]
    distance = abs(x) + abs(y)
    if nearest is None or nearest > distance:
        nearest = distance
        # nearestPoint = (x, y)
    steps = crossings[crossing]
    if leastSteps is None or leastSteps > steps:
        leastSteps = steps


print("Nearest crossing: " + str(nearest))
print("Least steps: " + str(leastSteps))
