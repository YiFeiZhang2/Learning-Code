# helper methods
# method to tell if an array is in the terminal state
# State class
import math

class State:
    def __init__ (self, arr, reward = None):
        if reward == None:
            self.state = arr[:9]
            self.reward = arr[-1]
        else:
            self.reward = reward
            self.state = []
            for x in arr:
                self.state.append(x)

# generates the list of resultant state after the player makes a move
def genNextStates(arr, player):
    print(arr)
    states = []
    for i in range(len(arr)):
        if arr[i] == 0:
            temp_arr = [x for x in arr]
            temp_arr[i] = player
            states.append(temp_arr)
    return states

def rowComplete(state):
    rows = [0, 3, 6]
    for r in rows:
        if state[r] != '0':
            if state[r] == state[r+1] == state[r+2]:
                return True
    return False

def colComplete(state):
    cols = [0, 1, 2]
    for c in cols:
        if state[c] != '0':
            if state[c] == state[c+3] == state[c+6] and state[c] != 0:

                return True
    return False

def diaComplete(state):
    if ((state[0] == state[4] == state[8]) or (state[2] == state[4] == state[6])) and state[4] != '0':
        return True
    return False

def isComplete(state):
    full = True
    for x in state:
        if x == '0' or x == 0:
            full = False
    return (full or rowComplete(state) or colComplete(state) or diaComplete(state))

def binSearch(arr, s, e, obj):
    if s > e:
        return -1
    m = math.floor((s+e) / 2)
    #print(arr[m].state_num)
    if obj == arr[m].state_num:
        return m
    elif obj < arr[m].state_num:
        return binSearch(arr, s, m-1, obj)
    else:
        return binSearch(arr, m+1, e, obj)