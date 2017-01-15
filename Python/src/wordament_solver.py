#!/usr/local/bin/python3
import sys
import os
import copy
import time

dir = "/Users/yili/Documents/Richard USB info/Learning-Code/Python/english-words-master/"
f_list=["dict_a.txt", "dict_b.txt", "dict_c.txt", "dict_d.txt", "dict_e.txt", "dict_f.txt", "dict_g.txt", "dict_h.txt", "dict_i.txt", "dict_j.txt", "dict_k.txt", "dict_l.txt", "dict_m.txt", "dict_n.txt", "dict_o.txt", "dict_p.txt", "dict_q.txt", "dict_r.txt", "dict_s.txt", "dict_t.txt", "dict_u.txt", "dict_v.txt", "dict_w.txt", "dict_x.txt", "dict_y.txt", "dict_z.txt"]

word_list = [list(input()) for i in range (4)]

word_dict = []
for i in range(len(f_list)):
    f = open(os.path.join(dir, f_list[i]))
    word_dict.append(f.read().split('\n'))
    f.close()

def bin_search(word, arr, hi, lo):
    if (lo > hi):
        return -1
    else:
        mid = (hi+lo) // 2
        if word == arr[mid]:
            return arr[mid]
        elif word > arr[mid]:
            return bin_search(word, arr, hi, mid+1)
        else:
            return bin_search(word, arr, mid-1, lo)
  

def solver (word_list, word_dict, path_list, i, j, used_ind):
    if (i < 0 or i > 3 or j < 0 or j > 3):
        return None
    elif ([i,j] in used_ind):
        return None
    elif (len(path_list) > 7):
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
        
        curr_word = ''.join(path_list).strip()
        ind = ord(curr_word[0])-97

        found = bin_search(curr_word, word_dict[ind], len(word_dict[ind])-1, 0)

        if (found != -1):
            output_list.append(found)

        return output_list

output = list()

start_time = time.time()

for i in range(4):
    for j in range(4):
        ans = solver (word_list, word_dict, [], i, j, [])
        if ans != None:
            output.extend(ans)

output = list(set(output))

output_filtered = sorted([x for x in output if len(x) > 2], key=len, reverse=True)

print(output_filtered)
print("%s" % (time.time()-start_time))