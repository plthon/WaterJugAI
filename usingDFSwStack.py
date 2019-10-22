class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def checkIfEncountered(stackX):
    if stackX not in alEn:
        stack.push(stackX)
        alEn.append(stackX)
        currentLevel = keepsTrackOfCurrentLevel.pop()
        keepsTrackOfCurrentLevel.push(currentLevel + 1)
        print(stackX)
        if stackX[0] == X and stackX[1] == Y and stackX[2] == Z:
            print("Completed")
            solvedX = True
            return True
    return False


def main():
    stack.push(CuSta)
    alEn.append(CuSta)
    keepsTrackOfCurrentLevel.push(0)
    # solved = False
    steps = 0

    while not stack.isEmpty():
        if solvedX:
            break
        steps += 1
        tempint = 0
        currentStack = stack.pop()
        a = currentStack[0]
        b = currentStack[1]
        c = currentStack[2]

        if a >= 0:
            # empty A to ground
            if checkIfEncountered((0, b, c)):
                break
            # fill a
            if a < B1:
                if checkIfEncountered((B1, b, c)):
                    break
            # empty a into b
            if a + b <= B2:
                if checkIfEncountered((0, a + b, c)):
                    break
            if a + b >= B2:
                if checkIfEncountered((a - (B2 - b), B2, c)):
                    break
            # empty a into c
            if a + c <= B3:
                if checkIfEncountered((0, b, a + c)):
                    break
            if a + c >= B3:
                if checkIfEncountered((a - (B3 - c), b, B3)):
                    break

        if b >= 0:
            if checkIfEncountered((a, 0, c)):
                break
            # fill a
            if b < B2:
                if checkIfEncountered((a, B2, c)):
                    break
            # empty b into a
            if a + b <= B1:
                if checkIfEncountered((a + b, 0, c)):
                    break
            if a + b >= B1:
                if checkIfEncountered((B1, b - (B1 - a), c)):
                    break
            # empty b into c
            if b + c <= B3:
                if checkIfEncountered((a, 0, b + c)):
                    break
            if b + c >= B3:
                if checkIfEncountered((a, b - (B3 - c), B3)):
                    break

        # empty jug c
        if c >= 0:
            if checkIfEncountered((a, b, 0)):
                break
            # fill a
            if c < B3:
                if checkIfEncountered((a, b, B3)):
                    break
            # empty c into a
            if a + c <= B1:
                if checkIfEncountered((a + c, b, 0)):
                    break
            if a + c >= B1:
                if checkIfEncountered((B1, b, c - (B1 - a))):
                    break
            # empty c into b
            if b + c <= B2:
                if checkIfEncountered((a, b + c, 0)):
                    break
            if b + c >= B2:
                if checkIfEncountered((a, B2, c - (B2 - b))):
                    break


"""
        if a > 0:
            currentStack = (0, b, c)
            if checkIfEncountered(currentStack):
                print(currentStack)
                keepsTrackOfCurrentLevel.push(currentLevel + 1)
        elif a < B1:
            currentStack = (B1, b, c)
            if checkIfEncountered(currentStack):
                print(currentStack)
                keepsTrackOfCurrentLevel.push(currentLevel + 1)
        elif a + b <= B2:
            currentStack = (0, a + b, c)
            if checkIfEncountered(currentStack):
                print(currentStack)
                keepsTrackOfCurrentLevel.push(currentLevel + 1)
        elif a + b > B2:
            currentStack = (a - (B2 - b), B2, c)
            if checkIfEncountered(currentStack):
                print(currentStack)
                keepsTrackOfCurrentLevel.push(currentLevel + 1)
        elif a + c <= B3:
            currentStack = (0, b, c + a)
            if checkIfEncountered(currentStack):
                print(currentStack)
                keepsTrackOfCurrentLevel.push(currentLevel + 1)
        elif a + c > B3:
            currentStack = (a - (B3 - c), b, B3)
            if checkIfEncountered(currentStack):
                print(currentStack)
                keepsTrackOfCurrentLevel.push(currentLevel + 1)

        elif b > 0:
            currentStack = (a, 0, c)
            if checkIfEncountered(currentStack):
                print(currentStack)
                keepsTrackOfCurrentLevel.push(currentLevel + 1)
        elif b < B2:
            currentStack = (a, B2, c)
            if checkIfEncountered(currentStack):
                print(currentStack)
                keepsTrackOfCurrentLevel.push(currentLevel + 1)
        elif b + a <= B1:
            currentStack = (a + b, 0, c)
            if checkIfEncountered(currentStack):
                print(currentStack)
                keepsTrackOfCurrentLevel.push(currentLevel + 1)
        elif b + a > B1:
            currentStack = (B1, b - (B1 - a), c)
            if checkIfEncountered(currentStack):
                print(currentStack)
                keepsTrackOfCurrentLevel.push(currentLevel + 1)
        elif b + c <= B3:
            currentStack = (a, 0, c + b)
            if checkIfEncountered(currentStack):
                print(currentStack)
                keepsTrackOfCurrentLevel.push(currentLevel + 1)
        elif b + c > B3:
            currentStack = (a, b - (B3 - c), B3)
            if checkIfEncountered(currentStack):
                print(currentStack)
                keepsTrackOfCurrentLevel.push(currentLevel + 1)

        elif c > 0:
            currentStack = (a, b, 0)
            if checkIfEncountered(currentStack):
                print(currentStack)
                keepsTrackOfCurrentLevel.push(currentLevel + 1)
        elif c < B3:
            currentStack = (a, b, B3)
            if checkIfEncountered(currentStack):
                print(currentStack)
                keepsTrackOfCurrentLevel.push(currentLevel + 1)
        elif a + c <= B1:
            currentStack = (a + c, b, 0)
            if checkIfEncountered(currentStack):
                print(currentStack)
                keepsTrackOfCurrentLevel.push(currentLevel + 1)
        elif a + c > B1:
            currentStack = (B1, B2, c - (B1 - a))
            if checkIfEncountered(currentStack):
                print(currentStack)
                keepsTrackOfCurrentLevel.push(currentLevel + 1)
        elif c + b <= B2:
            currentStack = (a, b + c, 0)
            if checkIfEncountered(currentStack):
                print(currentStack)
                keepsTrackOfCurrentLevel.push(currentLevel + 1)
        elif c + b > B2:
            currentStack = (a, B2, c - (B2 - b))
            if checkIfEncountered(currentStack):
                print(currentStack)
                keepsTrackOfCurrentLevel.push(currentLevel + 1)
"""

B1 = 10
B2 = 6
B3 = 5
x = 3
y = 0
z = 0
X = 7
Y = 0
Z = 0

stack = Stack()
keepsTrackOfCurrentLevel = Stack()
CuSta = (x, y, z)
alEn = []
level = 0
solvedX = False

main()
