

with open('day4in.txt') as f:
    lines = f.readlines()

alphabet = 'abcdefghijklmnopqrstuvwxyz'


class Room:
    def __init__(self, input):
        self.input = input
        self.id = 0
        self.keys = {}
        self.max_keys = []
        self.raw_text = ""
        self.parse_input()

    def parse_input(self):
        # print(self.input)
        self.id = int(self.input.split('-')[-1].split('[')[0])
        self.raw_text = self.input.replace('-', '').split(str(self.id))[0]
        keys = self.input.split('[')[1].split(']')[0]
        for key in keys:
            self.max_keys.append(key)

    def count_keys(self):
        for char in self.raw_text:
            if char in self.keys:
                self.keys[char] += 1
            else:
                self.keys[char] = 1

    def check_keys_order(self):
        keys = []
        vals = []
        for key in self.keys:
            keys.append(key)
            vals.append(self.keys[key])

        sort(keys, vals)

        for index in range(len(vals)):
            if self.values[key] < self.values[key+1]:
                return False
            if self.values[key] == self.values[key+1]:
                if alphabet.index(self.keys[key]) > alphabet.index(self.keys[key+1]):
                    return False
        return True

# print(f'{room.input}\n{room.id}\n{room.raw_text}\n{room.keys}')


def sort(k, v):
    for i in range(len(k)-1):
        for j in range(i+1, len(k)):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]
                k[i], k[j] = k[j], k[i]

    for i in range(max(v)):
        for j in range(len(k)):
            if v[j] == i:
                pass


sum = 0
for line in lines:
    room = Room(line.replace('\n', '').lower())
    room.count_keys()
    if (room.check_keys_order()):
        sum += room.id
    else:
        print(room.keys)
print(sum)
