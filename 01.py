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

lock = Lock()

number_of_zeros = 0
with open('input.txt', 'r') as input_file:
    for rotation in input_file:
        if lock.rotate(rotation) == 0:
            number_of_zeros += 1

print('Result: ', number_of_zeros)
