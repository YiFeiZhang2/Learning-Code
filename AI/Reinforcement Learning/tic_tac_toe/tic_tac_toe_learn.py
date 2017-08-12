from helper_methods import *
from random import random
from agent import *
#from time import *
state_file = 'states.txt'
circle_states = 'circle_values.txt'
cross_states = 'cross_values.txt'
CIRCLE = 1
CROSS = 2

class Environment:
    def __init__ (self, all_states):
        self.states = all_states

    # moves is the number of moves that has occured to reach the state
    def getReward (self, state, moves):
        states = self.states[moves]
        for s in states:
            if s.state == state:
                return s.reward
        return 'life sucks'

f = open(state_file, 'r')
all_lines = f.readlines()
split_lines = [line.split('|') for line in all_lines]
all_state = [[] for i in range(10)]
for i in range(len(split_lines)):
    for j in range(len(split_lines[i])):
        if split_lines[i][j] != '\n':
            all_state[i].append(State(split_lines[i][j]))

E = Environment(all_state)
# B2 represents cross player
# A1 represents circle player
B2 = Agent(all_state, CROSS)
A1 = Agent(all_state, CIRCLE)

# AI plays vs itself to learn
for i in range(1000000):
    # Keeps track of states that occured in this game for CIRCLE
    circle_game_states = []
    # Keeps track of states that occured in this game for CROSS
    cross_game_states = []
    cur_state = 0
    turn = 1

    init_state = [0,0,0,0,0,0,0,0,0]

    # CIRCLE goes first
    cur_state = A1.choose(init_state)
    circle_game_states.append(int(cur_state))
    while (not isComplete(cur_state)):
        turn += 1
        if turn%2 == 1:
            # print('Circle Choose')
            cur_state = A1.choose([int(x) for x in cur_state])
            circle_game_states.append(int(cur_state))
        else:
            # print('Cross Choose')
            cur_state = B2.choose([int(x) for x in cur_state])
            cross_game_states.append(int(cur_state))
        # print('cur state is: ' + cur_state)

    # print(circle_game_states)
    # print(cross_game_states)


    # print('TIME TO LEARN!!')
    winner = getWinner(cur_state)
    # print('winner is ' + str(winner))
    #If turn == odd, then CIRCLE made last move, thus won or tied
    A1.learn(circle_game_states, winner, E, turn)
    B2.learn(cross_game_states, winner, E, turn)

f = open(circle_states, 'w')
for s in A1.estimates:
    f.write(str(s.state_num) + ',' + str(s.value) + ',' + str(s.num_seen) + '\n')
f.close()

f = open(cross_states, 'w')
for s in B2.estimates:
    f.write(str(s.state_num) + ',' + str(s.value) + ',' + str(s.num_seen) + '\n')
f.close()
