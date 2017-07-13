from helper_methods import *
#from time import *
state_file = 'config.txt'
CIRCLE = 1
CROSS = 2

class Environment:
    def __init__ (self, all_states):
        self.states = all_states

class AgentValues:
    def __init__ (self, state_num, value, num_seen = 1):
        self.state_num = state_num
        self.value = value
        self.num_seen = num_seen

class Agent:
    def __init__ (self, init_estimates, player):
        # player value is either circle (1) or cross (2)
        self.player = player 
        # 9D array for the state 
        #self.estimates = [[[[[[[[[AgentValues(0, 0) for a in range(3)] for i in range(3)] for j in range(3)] for k in range(3)] for l in range(3)] for m in range(3)] for n in range(3)] for x in range(3)] for y in range(3)]
        # Alternatively, juat one array
        self.estimates = []
        for line in init_estimates:
            for s in line:
                self.estimates.append(AgentValues(int(s.state), 0))
        self.estimates.sort(key = lambda x: int(x.state_num))

    # Takes an array of the different positions that occured in the game, the end reward,
    # and updates the values associated for each position
    def learn (self, game_states, end_reward):
        # Set the end value to be the reward (either 1 for winning, or -1 for losing)
        next_ind = binSearch(self.estimates, 0, len(self.estimates), game_states[-1])
        if ind != -1:
            self.estimates[next_ind] = end_reward

        game_length = len(game_states)
        for i in range(game_length-2, -1, -1):
            cur_ind = binSearch(self.estimates, 0, len(self.estimates), game_states[i])
            self.estimates[cur_ind].value = self.estimates[cur_ind].value + (1 / self.estimates[cur_ind].num_seem) * (self.estimates[next_ind].value - self.estimates[cur_ind].value)
            next_ind = cur_ind

    def choose(self, cur_state):
        # Generates the indices of the future states
        actions_indices = [binSearch(self.estimates, 0, len(self.estimates), s) for s in genNextStates(cur_state, self.player)]

f = open(state_file, 'r')
all_lines = f.readlines()
split_lines = [line.split('|') for line in all_lines]
all_state = [[] for i in range(10)]
for i in range(len(split_lines)):
    for j in range(len(split_lines[i])):
        if split_lines[i][j] != '\n':
            all_state[i].append(State(split_lines[i][j]))

E = Environment(all_state)
A = Agent(all_state, CROSS)

# Keeps track of states that occured in this game for CIRCLE
circle_game_states = []
# Keeps track of states that occured in this game for CROSS
cross_game_states = []