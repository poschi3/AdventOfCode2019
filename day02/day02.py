import math

class Machine:
    def __init__(self, input, noun, verb):
        self.opcodes = [int(x) for x in input.split(",")]
        self.opcodes[1] = noun
        self.opcodes[2] = verb
    
    def calc(self):
        i = 0
        while True:
            opcode = self.opcodes[i]

            if opcode == 99:
                return self.opcodes[0]

            first = self.opcodes[self.opcodes[i+1]]
            second = self.opcodes[self.opcodes[i+2]]

            result = None
            if opcode == 1:
                result = first + second
            elif opcode == 2:
                result = first * second
            else:
                raise Exception('Unknown opcode ' + str(opcode) + ' on position ' + str(i))
            
            self.opcodes[self.opcodes[i+3]] = result
            i = i + 4

with open('input.txt') as file:
    input = file.readline().strip()

first = Machine(input, 12, 2)
result = first.calc()
print("First: " + str(result))

for noun in range(0, 100):
    for verb in range(0, 100):
        second = Machine(input, noun, verb)
        result = second.calc()
        if result == 19690720:
            print("Second : " + str(result) + " with " + str(noun) + " and " + str(verb))
            print("Answer is " + str(100 * noun + verb))
