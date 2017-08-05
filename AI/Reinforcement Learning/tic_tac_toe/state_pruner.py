# creates all possible board configurations and saves in config.txt
from helper_methods import *

CIRCLE = 1
CROSS = 2
filename = 'config.txt'
out_file = 'states.txt'
turns = [[] for i in range(10)]

# Takes a state in the form of a string, outputs number of turns to get to that state
# Eg: 000000000 = 0, 100000000000 = 1, 221112211 = 9
def turnGetter(s):
    t = 0
    for val in s:
        if val == '1' or val == '2':
            t += 1
    return t

# Takes a state in the form of a string, output whether the state for tic tac toe is valid
# A valid state is one where absolute difference between number of 1s and 2s in the state is at most 1
def validState(s):
    diff = 0
    for i in s:
        if i == '1':
            diff += 1
        elif i == '2':
            diff -= 1
        else:
            continue
    return (abs(diff) <= 1)

f = open(filename, 'r')
for line in f:
    # gets rid of the newline at end of each line
    line = line[:-1]
    # checks for length of state
    if len(line) != 9:
        continue
    if not validState(line):
        continue
    if rowComplete(line) or colComplete(line) or diaComplete(line):
        turns[turnGetter(line)].append(line+'1')
    else:
        turns[turnGetter(line)].append(line+'0')
f.close()

f = open(out_file, 'w')
for line in turns:
    for state in line:
        f.write(state+'|')
    f.write('\n')
f.close()
        

