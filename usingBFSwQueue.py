class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def add(self,item):
        self.items.insert(0, item)
    def get(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)


class Bottle:
    def __init__(self, xx, yy, zz):
        self.x = xx
        self.y = yy
        self.z = zz


def checkIfEncountered(bottle):
    if bottle not in alreadyEncountered:
        queue.add(bottle)
        alreadyEncountered.append(bottle)
        memory.append(MEMORY[le])
        return True
    return False


def main():
    bottle = Bottle(x, y, z)
    queue.add(bottle)
    alreadyEncountered.append(bottle)
    level = 1
    memory.append(bottle)
    MEMORY[level] = memory
    flag = False
    print(MEMORY)
    while not queue.isEmpty():
        bottle = queue.get()

        # If all nodes in current level explored.
        if bottle.x == -1 and bottle.y == -1 and bottle.z == -1:
            level += 1
            queue.add(bottle(-1, -1, -1))
            continue

        # If all bottles achieve required litres
        if bottle.x == X and bottle.y == Y and bottle.z == Z:
            break

        # If no possible solution
        # TODO exit when no possible solution





B1 = 10
B2 = 6
B3 = 5
x = 3
y = 0
z = 0
X = 7
Y = 0
Z = 0
queue = Queue()
alreadyEncountered = []
MEMORY = {}
memory = []

main()
