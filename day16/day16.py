class packet:
    def __init__(self, version, type, literal=None):
        self.version = version
        self.type = type
        self.literal = literal
        self.subpackets = list()

    def add_subpacket(self, subpacket):
        self.subpackets.append(subpacket)

    def sum_version(self):
        return self.version + sum([packet.sum_version() for packet in self.subpackets])

    def evaluate(self):
        if self.type == 4:
            return self.literal
        elif self.type == 0:
            return sum([subpacket.evaluate() for subpacket in self.subpackets])
        elif self.type == 1:
            result = 1
            for subpacket in self.subpackets:
                result *= subpacket.evaluate()
            return result
        elif self.type == 2:
            return min([packet.evaluate() for packet in self.subpackets])
        elif self.type == 3:
            return max([packet.evaluate() for packet in self.subpackets])
        elif self.type == 5:
            return int(self.subpackets[0].evaluate() > self.subpackets[1].evaluate())
        elif self.type == 6:
            return int(self.subpackets[0].evaluate() < self.subpackets[1].evaluate())
        elif self.type == 7:
            return int(self.subpackets[0].evaluate() == self.subpackets[1].evaluate())


code = ''

with open('day16.txt') as infile:
    for line in infile:
        code += str(bin(int(line.strip(), base=16)))
    code = code[2:]

while len(code) % 4 != 0:
    code = '0' + code


def parse_version_nr(index):
    nr = int(code[index:index + 3], base=2)
    return nr, index + 3


def parse_type(index):
    type = int(code[index:index + 3], base=2)
    return type, index + 3


def parse_quintet(index):
    quintet = code[index:index + 5]
    return quintet, index + 5


def parse_literal(index):
    quintet_list = list()
    going = True

    while going:
        quintet, index = parse_quintet(index)
        quintet_list.append(quintet[1:])
        going = quintet[0] == '1'

    return int(''.join(quintet_list), base=2), index


def parse_length_type(index):
    type = code[index]
    return int(type), index + 1


def parse_subpackets_length(index):
    length = code[index:index + 15]
    return int(length, base=2), index + 15


def parse_nr_subpackets(index):
    amount = code[index:index + 11]
    return int(amount, base=2), index + 11


def parse_operator(index):
    length_type, index = parse_length_type(index)
    if length_type == 0:
        subpackets_length, index = parse_subpackets_length(index)
        limit = index + subpackets_length
        subpackets = list()
        
        while index < limit:
            subpacket, index = parse_packet(index)
            subpackets.append(subpacket)
        
        return subpackets, index
    else:
        nr_subpackets, index = parse_nr_subpackets(index)
        subpackets = list()
        for _ in range(nr_subpackets):
            subpacket, index = parse_packet(index)
            subpackets.append(subpacket)
        
        return subpackets, index


def parse_packet(index):
    version_nr, index = parse_version_nr(index)
    type, index = parse_type(index)
    if type == 4:
        literal, index = parse_literal(index)
        return packet(version_nr, type, literal), index
    else:
        new_packet = packet(version_nr, type)
        subpackets, index = parse_operator(index)
        for subpacket in subpackets:
            new_packet.add_subpacket(subpacket)
        return new_packet, index


def part1():
    index = 0
    packet, _ = parse_packet(index)
    print(f'Solution for part 1 is {packet.sum_version()}')


def part2():
    index = 0
    packet, _ = parse_packet(index)
    print(f'Solution for part 2 is {packet.evaluate()}')

part1()
part2()