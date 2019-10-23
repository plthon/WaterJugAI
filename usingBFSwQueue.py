class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def add(self, item):
        self.items.insert(0, item)

    def get(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Bottle:
    def __init__(self, xx, yy, zz, bottle):
        self.x = xx
        self.y = yy
        self.z = zz
        self.previousBottle = bottle


def checkIfEncountered(bottle):
    if bottle not in alreadyEncountered:
        queue.add(bottle)
        alreadyEncountered.append(bottle)


def allPossibleRules(bottle):
    node = 1
    # Fill X
    if bottle.x < B1:
        node += 1
        checkIfEncountered(Bottle(B1, bottle.y, bottle.z, bottle))

    # Fill Y
    if bottle.y < B2:
        node += 1
        checkIfEncountered(Bottle(bottle.x, B2, bottle.z, bottle))

    # Fill Z
    if bottle.z < B3:
        node += 1
        checkIfEncountered(Bottle(bottle.x, bottle.y, B3, bottle))

    # Empty X
    if bottle.x > 0:
        node += 1
        checkIfEncountered(Bottle(0, bottle.y, bottle.z, bottle))

    # Empty Y
    if bottle.y > 0:
        node += 1
        checkIfEncountered(Bottle(bottle.x, 0, bottle.z, bottle))

    # Empty Z
    if bottle.z > 0:
        node += 1
        checkIfEncountered(Bottle(bottle.x, bottle.y, 0, bottle))

    # Pour X to Y when X + Y <= B2
    if bottle.x + bottle.y <= B2 and bottle.x != 0:
        node += 1
        checkIfEncountered(Bottle(0, bottle.y + bottle.x, bottle.z, bottle))

    # Pour X to Y when X + Y >= B2
    if bottle.x + bottle.y >= B2 and bottle.x != 0:
        node += 1
        checkIfEncountered(Bottle(bottle.x - (B2 - bottle.y), B2, bottle.z, bottle))

    # Pour X to Z when X + Z <= B3
    if bottle.x + bottle.z <= B3 and bottle.x != 0:
        node += 1
        checkIfEncountered(Bottle(0, bottle.y, bottle.z + bottle.x, bottle))

    # Pour X to Z when X + Z >= B3
    if bottle.x + bottle.z >= B3 and bottle.x != 0:
        node += 1
        checkIfEncountered(Bottle(bottle.x - (B3 - bottle.z), bottle.y, B3, bottle))

    # Pour Y to X when Y + X <= B1
    if bottle.y + bottle.x <= B1 and bottle.y != 0:
        node += 1
        checkIfEncountered(Bottle(bottle.x + bottle.y, 0, bottle.z, bottle))

    # Pour Y to X when Y + X >= B1
    if bottle.y + bottle.x >= B1 and bottle.y != 0:
        node += 1
        checkIfEncountered(Bottle(B1, bottle.y - (B1 - bottle.x), bottle.z, bottle))

    # Pour Y to Z when Y + Z <= B3
    if bottle.y + bottle.z <= B3 and bottle.y != 0:
        node += 1
        checkIfEncountered(Bottle(bottle.x, 0, bottle.z + bottle.y, bottle))

    # Pour Y to Z when Y + Z >= B3
    if bottle.y + bottle.z >= B3 and bottle.y != 0:
        node += 1
        checkIfEncountered(Bottle(bottle.x, bottle.y - (B3 - bottle.z), B3, bottle))

    # Pour Z to X when Z + X <= B1
    if bottle.z + bottle.x <= B1 and bottle.z != 0:
        node += 1
        checkIfEncountered(Bottle(bottle.x + bottle.z, bottle.y, 0, bottle))

    # Pour Z to X when Z + X >= B1
    if bottle.z + bottle.x >= B1 and bottle.z != 0:
        node += 1
        checkIfEncountered(Bottle(B1, bottle.y, bottle.z - (B1 - bottle.x), bottle))

    # Pour Z to Y when Z + Y <= B2
    if bottle.z + bottle.x <= B2 and bottle.z != 0:
        node += 1
        checkIfEncountered(Bottle(bottle.x, bottle.y + bottle.z, 0, bottle))

    # Pour Z to Y when Z + Y >= B2
    if bottle.z + bottle.x >= B2 and bottle.z != 0:
        node += 1
        checkIfEncountered(Bottle(bottle.x, B2, bottle.z - (B2 - bottle.y), bottle))


def main():
    bottle = Bottle(a, b, c, None)
    queue.add(bottle)
    alreadyEncountered.append(bottle)
    # MEMORY[1] = [[bottle]]
    while not queue.isEmpty():
        bottle = queue.get()

        # If all bottles achieve required litres
        if bottle.x == X and bottle.y == Y and bottle.z == Z:
            bottleList = []
            while bottle:
                bottleList.append(bottle)
                bottle = bottle.previousBottle

            bottleList.reverse()
            n = 1
            for item in bottleList:
                print(n, ": ", item.x, " | ", item.y, " | ", item.z, "\n")
                n += 1
            break

        # If no possible solution
        # TODO exit when no possible solution

        allPossibleRules(bottle)


B1 = 10
B2 = 6
B3 = 5
a = 2
b = 0
c = 0
X = 4
Y = 0
Z = 0
queue = Queue()
alreadyEncountered = []
main()
