from copy import deepcopy

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
    def __init__(self, xx, yy, zz, bottleList):
        self.x = xx
        self.y = yy
        self.z = zz
        self.parent = bottleList

    def getID(self):
        return [self.x, self.y, self.z]


def checkIfEncountered(bottle, level):
    if bottle not in alreadyEncountered:
        queue.add(bottle)
        alreadyEncountered.append(bottle)
        allKeys = list(MEMORY.keys())

        index = 0

        for parentList in MEMORY[level]:
            if parentList[-1].getID() == bottle.parent:
                tempMemory = []
                for item in MEMORY.get(level)[index]:
                    tempMemory.append(item)
                tempMemory.append(bottle)
                index += 1
                if level + 1 in allKeys:
                    MEMORY[level + 1].append(tempMemory)
                else:
                    MEMORY[level + 1] = [tempMemory]
                break
        return True
    return False


def main():
    bottle = Bottle(a, b, c, ["Initial"])
    queue.add(bottle)
    alreadyEncountered.append(bottle)
    MEMORY[1] = [[bottle]]
    level = 1
    # flag = False
    parentBottle = bottle
    while not queue.isEmpty():
        bottle = queue.get()

        """
        # If all nodes in current level explored.
        if bottle.x == -1 and bottle.y == -1 and bottle.z == -1:
            level += 1
            queue.add(bottle(-1, -1, -1))
            continue
        """

        # If all bottles achieve required litres
        if bottle.x == X and bottle.y == Y and bottle.z == Z:
            for list1 in MEMORY:
                for list2 in MEMORY[list1]:
                    if list2[-1].getID() == [X, Y, Z]:
                        itemLevel = 0
                        for item in list2:
                            print(itemLevel, ": " + item.x, " | ", item.y, " | ", item.z, "\n")
                            itemLevel += 1
                        break
            break

        # If no possible solution
        # TODO exit when no possible solution

        # Fill X
        if bottle.x < B1:
            checkIfEncountered(Bottle(B1, bottle.y, bottle.z, parentBottle.getID()), level)

        # Fill Y
        if bottle.y < B2:
            checkIfEncountered(Bottle(bottle.x, B2, bottle.z, parentBottle.getID()), level)

        # Fill Z
        if bottle.z < B3:
            checkIfEncountered(Bottle(bottle.x, bottle.y, B3, parentBottle.getID()), level)

        # Empty X
        if bottle.x > 0:
            checkIfEncountered(Bottle(0, bottle.y, bottle.z, parentBottle.getID()), level)

        # Empty Y
        if bottle.y > 0:
            checkIfEncountered(Bottle(bottle.x, 0, bottle.z, parentBottle.getID()), level)

        # Empty Z
        if bottle.z > 0:
            checkIfEncountered(Bottle(bottle.x, bottle.y, 0, parentBottle.getID()), level)

        # Pour X to Y when X + Y <= B2
        if bottle.x + bottle.y <= B2 and bottle.x != 0:
            checkIfEncountered(Bottle(0, bottle.y + bottle.x, bottle.z, parentBottle.getID()), level)

        # Pour X to Y when X + Y >= B2
        if bottle.x + bottle.y >= B2 and bottle.x != 0:
            checkIfEncountered(Bottle(bottle.x - (B2 - bottle.y), B2, bottle.z, parentBottle.getID()), level)

        # Pour X to Z when X + Z <= B3
        if bottle.x + bottle.z <= B3 and bottle.x != 0:
            checkIfEncountered(Bottle(0, bottle.y, bottle.z + bottle.x, parentBottle.getID()), level)

        # Pour X to Z when X + Z >= B3
        if bottle.x + bottle.z >= B3 and bottle.x != 0:
            checkIfEncountered(Bottle(bottle.x - (B3 - bottle.z), bottle.y, B3, parentBottle.getID()), level)

        # Pour Y to X when Y + X <= B1
        if bottle.y + bottle.x <= B1 and bottle.y != 0:
            checkIfEncountered(Bottle(bottle.x + bottle.y, 0, bottle.z, parentBottle.getID()), level)

        # Pour Y to X when Y + X >= B1
        if bottle.y + bottle.x >= B1 and bottle.y != 0:
            checkIfEncountered(Bottle(B1, bottle.y - (B1 - bottle.x), bottle.z, parentBottle.getID()), level)

        # Pour Y to Z when Y + Z <= B3
        if bottle.y + bottle.z <= B3 and bottle.y != 0:
            checkIfEncountered(Bottle(bottle.x, 0, bottle.z + bottle.y, parentBottle.getID()), level)

        # Pour Y to Z when Y + Z >= B3
        if bottle.y + bottle.z >= B3 and bottle.y != 0:
            checkIfEncountered(Bottle(bottle.x, bottle.y - (B3 - bottle.z), B3, parentBottle.getID()), level)

        # Pour Z to X when Z + X <= B1
        if bottle.z + bottle.x <= B1 and bottle.z != 0:
            checkIfEncountered(Bottle(bottle.x + bottle.z, bottle.y, 0, parentBottle.getID()), level)

        # Pour Z to X when Z + X >= B1
        if bottle.z + bottle.x >= B1 and bottle.z != 0:
            checkIfEncountered(Bottle(B1, bottle.y, bottle.z - (B1 - bottle.x), parentBottle.getID()), level)

        # Pour Z to Y when Z + Y <= B2
        if bottle.z + bottle.x <= B2 and bottle.z != 0:
            checkIfEncountered(Bottle(bottle.x, bottle.y + bottle.z, 0, parentBottle.getID()), level)

        # Pour Z to Y when Z + Y >= B2
        if bottle.z + bottle.x >= B2 and bottle.z != 0:
            checkIfEncountered(Bottle(bottle.x, B2, bottle.z - (B2 - bottle.y), parentBottle.getID()), level)

        """
        # TODO something
        if not flag:
            queue.add(bottle(-1, -1, -1))
        flag = True
        """
        parentBottle = bottle
        level += 1  # Try


B1 = 10
B2 = 6
B3 = 5
a = 3
b = 0
c = 0
X = 7
Y = 0
Z = 0
queue = Queue()
alreadyEncountered = []
MEMORY = {}
main()
