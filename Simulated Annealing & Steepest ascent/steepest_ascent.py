def init():
    return [2, 1, 5, 0]

def state_Cost(state):
    count = 0
    len1 = len(state)
    for i in range(0, len1-1):
        for j in range(i + 1, len1):
            if state[i] > state[j]:
                count+=1
    return count


def goal_state(state):
    if state_Cost(state) == 0:
        return True
    else:
        return False


def new_state(current_state, current_cost):
    temp = current_state.copy()
    len2 = len(current_state)
    for i in range(0, len2 - 1):
        for j in range(i + 1, len2):
            temp[i], temp[j] = temp[j], temp[i]
            temp1 = state_Cost(temp)
            if temp1 < current_cost:
                return temp, temp1
        temp = current_state.copy()

    if temp1 >= current_cost:
        return current_state, None


def main():
    state = init()
    cost = state_Cost(state)
    while not goal_state(state):
        state, cost = new_state(state, cost)
        if cost is None:
            print(state)
            return

    print(state)
    return


if __name__ == '__main__':
    main()
