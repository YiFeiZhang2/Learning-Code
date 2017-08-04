# The agent has a choice among n different options
# Each choice gives a different numerical reward
# The goal is to maximize the expected total reward
# over x steps

# Next steps: effect of optimistic initial values
#             tracking non-stationary values
#             changing step sizes
#             fix softmax

import random
import math

# returns the indices in the arr that has the largest value
def max_indices(arr):
    indices = [arr[0]]
    max_val = arr[0]
    for i in range(1, len(arr)):
        if (arr[i] == max_val):
            indices.append(i)
        elif (arr[i] > max_val):
            indices = [i]
            max_val = arr[i]
    return indices

def ave_reward(bandit_arr):
    t = 0
    for i in range(len(bandit_arr)):
        t += bandit_arr[i].ave_reward
    return t / float(len(bandit_arr))

class Bandit:
    def __init__(self, num_arms, method):
        self.method = method
        self.estimates = [0] * num_arms   
        self.num_pulls = [0] * num_arms     
        self.total = 0
        self.ave_reward = 0

    # choose one of the bandit's arm based on the method
    # with the softmax, as temp -> inf, policy -> random, and as temp -> 0, policy -> greedy
    def choose_arm(self, arms, e_val = 0.1, temp = 0.1, e = 2.718):
        indices = max_indices(self.estimates)
        chosen_index = indices[random.randint(0, len(indices)-1)]
        if (self.method == 'e-greedy'):
            p = random.random()
            if (p <= e_val):
                w_indices = [x for x in range(0, len(arms)) if x != chosen_index]
                chosen_index = w_indices[random.randint(0, len(w_indices)-1)]
        elif (self.method == 'softmax'):
            # create distribution function
            denom = 0
            for i in range(len(arms)):
                denom += math.pow(e, (self.estimates[i] / temp))
            probs = [math.pow(e, (self.estimates[i] / temp)) / denom for i in range(len(arms))]
            distr = [0]*len(probs)
            for i in range(len(probs)):
                if i == 0:
                    distr[i] = probs[i]
                else:
                    distr[i] = distr[i-1] + probs[i]
            # choose index
            p = random.random()
            for i in range(len(distr)):
                if p < distr[i] and (i == 0 or p > distr[i-1]):
                    chosen_index = i
        return int(chosen_index)

    # given the chosen arm, update the agent's estimates
    def learn(self, arms, chosen_index):
        self.num_pulls[chosen_index] = self.num_pulls[chosen_index] + 1
        reward = arms[chosen_index] + random.gauss(0, 1)
        prev_estimate = self.estimates[chosen_index]
        self.estimates[chosen_index] = prev_estimate + (1/self.num_pulls[chosen_index]) * (reward - prev_estimate)
        self.total += reward
        self.ave_reward = float(self.total) / float(sum(self.num_pulls))

    # arms represents the actual values
    def bandit(self, arms, eval = 0.1):
        chosen_index = self.choose_arm(arms, eval)
        self.learn(arms, chosen_index)

num_tests = 100
num_arms = 10
time_steps = 1500
methods = ['greedy', 'e-greedy', 'softmax']

arms = [[random.gauss(0, 1) for x in range(num_arms)] for x in range(num_tests)]
b_greed = [Bandit(num_arms, methods[0]) for x in range(num_tests)]
b_egreed = [Bandit(num_arms, methods[1]) for x in range(num_tests)]
b_softmax = [Bandit(num_arms, methods[2]) for x in range(num_tests)]


for i in range(time_steps):
    for j in range(num_tests):
        b_greed[j].bandit(arms[j])
        b_egreed[j].bandit(arms[j])
        b_softmax[j].bandit(arms[j])
    if (i == 499):
        print('greedy ave reward at i = 500 is ' + str(ave_reward(b_greed)))
        print('egreedy ave reward at i = 500 is ' + str(ave_reward(b_egreed)))
        print('softmax ave reward at i = 500 is ' + str(ave_reward(b_softmax)))
    elif (i == 999):
        print('greedy ave reward at i = 1000 is ' + str(ave_reward(b_greed)))
        print('egreedy ave reward at i = 1000 is ' + str(ave_reward(b_egreed)))
        print('softmax ave reward at i = 1000 is ' + str(ave_reward(b_softmax)))
    elif (i == 1499):
        print('greedy ave reward at i = 1500 is ' + str(ave_reward(b_greed)))
        print('egreedy ave reward at i = 1500 is ' + str(ave_reward(b_egreed)))
        print('softmax ave reward at i = 1500 is ' + str(ave_reward(b_softmax)))
        # print(b_egreed[0].num_pulls)