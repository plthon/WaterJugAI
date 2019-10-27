"""
Thon Pun Liang 101209471
"""

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
    def __init__(self, xx, yy, zz, bottle, string):
        self.x = xx
        self.y = yy
        self.z = zz
        self.previousBottle = bottle
        self.action = string


def checkIfEncountered(bottle):
    bottleT = (bottle.x, bottle.y, bottle.z)
    if bottleT not in alreadyEncountered:
        queue.add(bottle)
        alreadyEncountered.append(bottleT)


def allPossibleRules(bottle):
    # Fill X
    if bottle.x < B1:
        checkIfEncountered(Bottle(B1, bottle.y, bottle.z, bottle, "Fill B1"))

    # Fill Y
    if bottle.y < B2:
        checkIfEncountered(Bottle(bottle.x, B2, bottle.z, bottle, "Fill B2"))

    # Fill Z
    if bottle.z < B3:
        checkIfEncountered(Bottle(bottle.x, bottle.y, B3, bottle, "Fill B3"))

    # Empty X
    if bottle.x > 0:
        checkIfEncountered(Bottle(0, bottle.y, bottle.z, bottle, "Empty B1"))

    # Empty Y
    if bottle.y > 0:
        checkIfEncountered(Bottle(bottle.x, 0, bottle.z, bottle, "Empty B2"))

    # Empty Z
    if bottle.z > 0:
        checkIfEncountered(Bottle(bottle.x, bottle.y, 0, bottle, "Empty B3"))

    # Pour X to Y when X + Y <= B2
    if bottle.x + bottle.y <= B2 and bottle.x != 0:
        checkIfEncountered(Bottle(0, bottle.y + bottle.x, bottle.z, bottle, "Pour from B1 to B2"))

    # Pour X to Y when X + Y >= B2
    if bottle.x + bottle.y >= B2 and bottle.x != 0:
        checkIfEncountered(Bottle(bottle.x - (B2 - bottle.y), B2, bottle.z, bottle, "Pour from B1 to B2"))

    # Pour X to Z when X + Z <= B3
    if bottle.x + bottle.z <= B3 and bottle.x != 0:
        checkIfEncountered(Bottle(0, bottle.y, bottle.z + bottle.x, bottle, "Pour from B1 to B3"))

    # Pour X to Z when X + Z >= B3
    if bottle.x + bottle.z >= B3 and bottle.x != 0:
        checkIfEncountered(Bottle(bottle.x - (B3 - bottle.z), bottle.y, B3, bottle, "Pour from B1 to B3"))

    # Pour Y to X when Y + X <= B1
    if bottle.y + bottle.x <= B1 and bottle.y != 0:
        checkIfEncountered(Bottle(bottle.x + bottle.y, 0, bottle.z, bottle, "Pour from B2 to B1"))

    # Pour Y to X when Y + X >= B1
    if bottle.y + bottle.x >= B1 and bottle.y != 0:
        checkIfEncountered(Bottle(B1, bottle.y - (B1 - bottle.x), bottle.z, bottle, "Pour from B2 to B1"))

    # Pour Y to Z when Y + Z <= B3
    if bottle.y + bottle.z <= B3 and bottle.y != 0:
        checkIfEncountered(Bottle(bottle.x, 0, bottle.z + bottle.y, bottle, "Pour from B2 to B3"))

    # Pour Y to Z when Y + Z >= B3
    if bottle.y + bottle.z >= B3 and bottle.y != 0:
        checkIfEncountered(Bottle(bottle.x, bottle.y - (B3 - bottle.z), B3, bottle, "Pour from B2 to B3"))

    # Pour Z to X when Z + X <= B1
    if bottle.z + bottle.x <= B1 and bottle.z != 0:
        checkIfEncountered(Bottle(bottle.x + bottle.z, bottle.y, 0, bottle, "Pour from B3 to B1"))

    # Pour Z to X when Z + X >= B1
    if bottle.z + bottle.x >= B1 and bottle.z != 0:
        checkIfEncountered(Bottle(B1, bottle.y, bottle.z - (B1 - bottle.x), bottle, "Pour from B3 to B1"))

    # Pour Z to Y when Z + Y <= B2
    if bottle.z + bottle.y <= B2 and bottle.z != 0:
        checkIfEncountered(Bottle(bottle.x, bottle.y + bottle.z, 0, bottle, "Pour from B3 to B2"))

    # Pour Z to Y when Z + Y >= B2
    if bottle.z + bottle.y >= B2 and bottle.z != 0:
        checkIfEncountered(Bottle(bottle.x, B2, bottle.z - (B2 - bottle.y), bottle, "Pour from B3 to B2"))


def main():
    bottle = Bottle(a, b, c, None, "Start State")
    queue.add(bottle)
    alreadyEncountered.append(bottle)
    while not queue.isEmpty():
        bottle = queue.get()

        # If all bottles achieve required litres
        if bottle.x == X and bottle.y == Y and bottle.z == Z:
            print("Solution is found!:\n\n"
                  "Max: ", B1, " | ", B2, " | ", B3, "\n")
            bottleList = []
            while bottle:
                bottleList.append(bottle)
                bottle = bottle.previousBottle

            bottleList.reverse()
            n = 1
            for item in bottleList:
                print(n, ": ", item.x, " | ", item.y, " | ", item.z, " | ", item.action, "\n")
                n += 1
            print("Goal state reached. Number of steps:", n-1)
            return True

        allPossibleRules(bottle)

    return False


def validateInput():
    B1 = int(input("Please enter Max Volume of Bottle 1: "))
    B2 = int(input("Please enter Max Volume of Bottle 2: "))
    B3 = int(input("Please enter Max Volume of Bottle 3: "))
    print()
    a = int(input("Please enter Start Volume of Bottle 1: "))
    b = int(input("Please enter Start Volume of Bottle 2: "))
    c = int(input("Please enter Start Volume of Bottle 3: "))
    print()
    X = int(input("Please enter Goal Volume of Bottle 1: "))
    Y = int(input("Please enter Goal Volume of Bottle 2: "))
    Z = int(input("Please enter Goal Volume of Bottle 3: "))
    print()

    if a > B1 or b > B2 or c > B3 or \
            X > B1 or Y > B2 or Z > B3:
        print("No possible solution!")
    else:
        return B1, B2, B3, a, b, c, X, Y, Z, True


B1, B2, B3, a, b, c, X, Y, Z, runnable = validateInput()
if runnable:
    print("Processing...\n")
    queue = Queue()
    alreadyEncountered = []
    solved = main()
    if not solved:
        print("No possible solution!")
