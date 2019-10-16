def get_all_states(state):
    # Let the 3 jugs be called a,b,c
    a = state[0]
    b = state[1]
    c = state[2]

    if a == X and b == Y and c == Z:
        ans.append(state)
        return True

    # if current state is already visited earlier
    if (a, b, c) in memory:
        return False

    memory[(a, b, c)] = 1

    # empty jug a
    if a >= 0:
        # empty A to ground
        if get_all_states((0, b, c)):
            ans.append(state)
            return True
        # fill a
        if a < B1:
            if get_all_states((B1, b, c)):
                ans.append(state)
                return True
        # empty a into b
        if a + b <= B2:
            if get_all_states((0, a + b, c)):
                ans.append(state)
                return True
        else:
            if get_all_states((a - (B2 - b), B2, c)):
                ans.append(state)
                return True
        # empty a into c
        if a + c <= B3:
            if get_all_states((0, b, a + c)):
                ans.append(state)
                return True
        else:
            if get_all_states((a - (B3 - c), b, B3)):
                ans.append(state)
                return True

    # empty jug b
    if b >= 0:
        if get_all_states((a, 0, c)):
            ans.append(state)
            return True
        # fill a
        if b < B2:
            if get_all_states((a, B2, c)):
                ans.append(state)
                return True
        # empty b into a
        if a + b <= B1:
            if get_all_states((a + b, 0, c)):
                ans.append(state)
                return True
        else:
            if get_all_states((B1, b - (B1 - a), c)):
                ans.append(state)
                return True
        # empty b into c
        if b + c <= B3:
            if get_all_states((a, 0, b + c)):
                ans.append(state)
                return True
        else:
            if get_all_states((a, b - (B3 - c), B3)):
                ans.append(state)
                return True

    # empty jug c
    if c >= 0:
        if get_all_states((a, b, 0)):
            ans.append(state)
            return True
        # fill a
        if c < B3:
            if get_all_states((a, b, B3)):
                ans.append(state)
                return True
        # empty c into a
        if a + c <= B1:
            if get_all_states((a + c, b, 0)):
                ans.append(state)
                return True
        else:
            if get_all_states((B1, b, c - (B1 - a))):
                ans.append(state)
                return True
        # empty c into b
        if b + c <= B2:
            if get_all_states((a, b + c, 0)):
                ans.append(state)
                return True
        else:
            if get_all_states((a, B2, c - (B2 - b))):
                ans.append(state)
                return True

    return False


def gettingInput():
    print("Please enter maximum capacity of bottles:")
    B1 = int(input("B1: "))
    B2 = int(input("B2: "))
    B3 = int(input("B3: "))

    print("\nPlease enter start state of bottles:")
    x = int(input("B1: "))
    y = int(input("B1: "))
    z = int(input("B1: "))

    print("\nPlease enter goal state of bottles:")
    X = int(input("B1: "))
    Y = int(input("B1: "))
    Z = int(input("B1: "))

    return B1, B2, B3, x, y, z, X, Y, Z


def main():
    initial_state = (x, y, z)
    print("\nStarting work...\n")
    get_all_states(initial_state)
    if len(ans) == 0:
        print("No Possible Solution!")
    else:
        ans.reverse()
        for i in ans:
            print(i)


# 3 water jugs capacity -> (x,y,z) where x>y>z
B1, B2, B3, x, y, z, X, Y, Z = gettingInput()
capacity = (B1, B2, B3)
# Maximum capacities of 3 jugs -> x,y,z
B1 = capacity[0]
B2 = capacity[1]
B3 = capacity[2]

# to mark visited states
memory = {}

# store solution path
ans = []

main()
