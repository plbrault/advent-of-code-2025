# Class Lock for part 1
"""
class Lock:
    INITIAL_POS = 50
    MAX_POS = 99

    def __init__(self):
        self.position = 50

    def rotate(self, rotation):
        position = self.position + 1
        max_pos = Lock.MAX_POS + 1

        direction = rotation[0]
        distance = int(rotation[1:])
        if distance >= max_pos:
            distance = distance % max_pos
        if direction == 'L':
            position -= distance
            if position <= 0:
                position += max_pos
        else:
            position += distance
            if position > max_pos:
                position -= max_pos
        
        self.position = position - 1
        return self.position
"""

# Class Lock for part 2
class Lock:
    INITIAL_POS = 50
    MAX_POS = 99

    def __init__(self):
        self.position = 50
        self.number_of_zeros = 0

    def rotate(self, rotation):
        direction = rotation[0]
        distance = int(rotation[1:])

        if direction == 'L':
            for i in range(distance):
                self.position -= 1
                if self.position == 0:
                    self.number_of_zeros += 1
                elif self.position < 0:
                    self.position = Lock.MAX_POS
        else:
            for i in range(distance):
                self.position += 1
                if self.position > Lock.MAX_POS:
                    self.position = 0
                    self.number_of_zeros += 1

lock = Lock()

with open('input.txt', 'r') as input_file:
    for rotation in input_file:
        lock.rotate(rotation)

print('Result: ', lock.number_of_zeros)
