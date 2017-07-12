from helper_methods import *
state_file = 'config.txt'

class Environment:
    def __init__ (self, all_states):
        self.states = all_states

class Agent:
    est_values = 5


f = open(state_file, 'r')
all_lines = f.readlines()
split_lines = [line.split('|') for line in all_lines]
all_state = [[] for i in range(10)]
for i in range(len(split_lines)):
    for j in range(len(split_lines[i])):
        if split_lines[i][j] != '\n':
            all_state[i].append(State(split_lines[i][j]))

E = Environment(all_state)