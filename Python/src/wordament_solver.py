#!/usr/local/bin/python3
import sys
import os
import copy
import time

dir = "/Users/yili/Documents/Richard USB info/Learning-Code/Python/english-words-master/"
file1="words.txt"
file2="words2.txt"
file3="words3.txt"

word_list = [list(input()) for i in range (4)]

f1 = open(os.path.join(dir, file1), 'r')
word_dict1 = f1.read().split('\n')

def solver (word_list, word_dict, path_list, i, j, used_ind):
    if (i < 0 or i > 3 or j < 0 or j > 3):
        return None
    elif ([i,j] in used_ind):
        return None
    elif (len(path_list) > 4):
        return None
    else:
        to_solve = [[i+1, j+1], [i-1, j-1], [i-1, j+1], [i+1, j-1], [i+1, j], [i-1, j], [i, j+1], [i, j-1]]
        path_list.append(word_list[i][j])
        used_ind.append([i,j])
        output_list = []

        for ind in to_solve:
            ans = solver (word_list, word_dict, copy.copy(path_list), ind[0], ind[1], copy.copy(used_ind))
            if ans != None:
                output_list.extend(ans)
        
        curr_word = ''.join(path_list)

        if  curr_word in word_dict:
            output_list.append(curr_word)

        return output_list

output = list()

start_time = time.time()

for i in range(4):
    for j in range(4):
        ans = solver (word_list, word_dict1, [], i, j, [])
        if ans != None:
            output.extend(ans)

output = list(set(output))

output_filtered = sorted([x for x in output if len(x) > 2], key=len, reverse=True)

print(output_filtered)
print("%s" % (time.time()-start_time))