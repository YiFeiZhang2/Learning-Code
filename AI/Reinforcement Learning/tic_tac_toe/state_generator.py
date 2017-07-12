# creates all possible board configurations and saves in config.txt
from helper_methods import *

CIRCLE = 1
CROSS = 2
init_state = [0,0,0,0,0,0,0,0,0]

# generates the list of resultant state after the player makes a move
def genNextStates(arr, player):
    states = []
    for i in range(len(arr)):
        if arr[i] == 0:
            temp_arr = [x for x in arr]
            temp_arr[i] = player
            states.append(temp_arr)
    return states

# states where circle has next move
circle_states = [[] for i in range(10)]
circle_states[0] = [State(init_state)]
# states where x has next move
cross_states = [[] for i in range(10)]
cross_states[0] = [State(init_state)]

for i in range(0, 9):
    for s in cross_states[i]:
        if (s.reward == 0):
            ns = genNextStates(s.state, CROSS)
            for n in ns:
                if isComplete(n):
                    circle_states[i+1].append(State(n, 1))
                else:
                    circle_states[i+1].append(State(n, 0))
    for s in circle_states[i]:
        ns = genNextStates(s.state, CIRCLE)
        for n in ns:
            if isComplete(n):
                cross_states[i+1].append(State(n, 1))
            else:
                cross_states[i+1].append(State(n, 0))

filename = 'config.txt'

f = open(filename, 'w')
for x in range(0, 10):
    for s in cross_states[x]:
        for i in s.state:
            f.write(str(i))
        f.write(str(s.reward))
        f.write('|')
    f.write('\n')
        

