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


def BFS(x, y, target):
    dict_ = {}  # tuple, int
    isSolvable = False
    path = []  # int, int
    queue = Queue()  # path
    lll = (0, 0)
    queue.add(lll)
    dict_[lll] = 0

    while not queue.isEmpty():
        bottle = queue.get()

        if dict_[bottle] == 1:
            continue

        if bottle[0] > x or bottle[1] > y or bottle[0] < 0 or bottle[1] < 0:
            continue

        path.append(bottle)
        dict_[bottle] = 1

        if bottle[0] == target or bottle[1] == target:
            isSolvable = True
            path.append(bottle)
            for x in path:
                print(x)
            break

        queue.add((bottle[0], x))
        queue.add((y, bottle[1]))

        temp = 0
        while temp <= x:
            c = bottle[0] + temp
            d = bottle[1] - temp

            if c == x or (d == 0 and d >= 0):
                queue.add((c, d))

            c = bottle[0] - temp
            d = bottle[1] + temp

            if d == y or (c == 0 and c >= 0):
                queue.add((c, d))

        queue.add((x, 0))
        queue.add(0, y)

    if not isSolvable:
        print("No solution")


BFS(4, 3, 2)
