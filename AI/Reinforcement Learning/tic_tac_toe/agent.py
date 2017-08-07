class AgentValues:
    def __init__ (self, state_num, value, num_seen = 1):
        self.state_num = state_num
        self.value = value
        self.num_seen = num_seen

class Agent:
    # n represents whether the agent is new, or information is already in the initial estimates
    def __init__ (self, init_estimates, player, n = True):
        # player value is either circle (1) or cross (2)
        self.player = player 
        # 9D array for the state s
        # Alternatively, juat one array
        self.estimates = []
        if (n):
            for line in init_estimates:
                for s in line:
                    self.estimates.append(AgentValues(int(s.state), 1))
            self.estimates.sort(key = lambda x: int(x.state_num))
        else:
            for line in init_estimates:
                [state, value, seen] = list(map(float, line.split(',')))
                self.estimates.append(AgentValues(int(state), value, int(seen)))
            self.estimates.sort(key = lambda x: int(x.state_num))

    # Takes an array of the different positions that occured in the game, the end reward,
    # and updates the values associated for each position
    # or last_move is false, so the Agent must have lost or tied
    def learn (self, game_states, winner, env, turns):
        # Set the end value to be the reward (either 1 for winning, or -1 for losing)
        next_ind = binSearch(self.estimates, 0, len(self.estimates), game_states[-1])
        if next_ind != -1:
            # print('game state is ' + str(game_states[-1]))

            # Environment only stores +1 for a winning state, but such a state is a loss for the other player
            # Winner gives reward of 2, losing gives reward of 0, tying vies 1
            if winner == self.player:
                self.estimates[next_ind].value = 2
            elif winner == 0:
                self.estimates[next_ind].value = 1
            else:
                self.estimates[next_ind].value = 0
            
            # print('reward is ' + str(self.estimates[next_ind].value))

        # print('at least we got this far')
        game_length = len(game_states)
        for i in range(game_length-2, -1, -1):
            cur_ind = binSearch(self.estimates, 0, len(self.estimates), game_states[i])
            self.estimates[cur_ind].value = self.estimates[cur_ind].value + (1 / self.estimates[cur_ind].num_seen) * (self.estimates[next_ind].value - self.estimates[cur_ind].value)
            # print('values is ' + str(self.estimates[cur_ind].value))
            next_ind = cur_ind

    # cur_state is the vector, represented by an array of characters
    # returns an string representing the state
    def choose(self, cur_state):
        # Generates the indices of the future states
        # Action stores the index that will be chosen
        action = -1
        action_indices = [binSearch(self.estimates, 0, len(self.estimates), int(''.join([str(t) for t in s]))) for s in genNextStates(cur_state, self.player)]
        # print('action indices are: ' + str(action_indices))

        denom = 0
        for i in action_indices:
            denom += math.pow(e, (self.estimates[i].value / temperature))
        probs = [math.pow(e, (self.estimates[i].value / temperature)) / denom for i in action_indices]
        distr = [0]*len(probs)
        for i in range(len(probs)):
            if i == 0:
                distr[i] = probs[i]
            else:
                distr[i] = distr[i-1] + probs[i]
        p = random()
        for i in range(len(distr)):
            if p < distr[i] and (i == 0 or p > distr[i-1]):
                action = action_indices[i]

        self.estimates[action].num_seen += 1
        output_state = self.estimates[action].state_num
        return ('{0:09d}'.format(output_state))
