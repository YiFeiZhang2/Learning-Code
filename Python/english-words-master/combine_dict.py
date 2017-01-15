#!/usr/local/bin/python3
#can make much more efficient 
#for each x in dict 1, check dict2[i] and dict3[j] for lexicographical comparison
#if either are same as x, then x+1
#if dict2[i] and dict3[j] and both larger, x+1
#else if dict2[i] is smaller, increment i, and if dict3[j] is smaller, increment j

import sys
import os
import re
import string

dir = "/Users/yili/Documents/Richard USB info/Learning-Code/Python/english-words-master/"
file1="words.txt"
file2="words2.txt"
file3="words3.txt"

f1 = open(os.path.join(dir, file1), 'r')
f2 = open(os.path.join(dir, file2), 'r')
f3 = open(os.path.join(dir, file3), 'r')

dict1 = f1.read().lower().split('\n')
dict2 = f2.read().lower().split('\n')
dict3 = f3.read().lower().split('\n')

f1.close()
f2.close()
f3.close()

output = list()

i=0
j=0
k=0

for i in range(len(dict1)):
    while dict1[i] > dict2[j] and j < len(dict2)-1:
        j += 1
    while dict1[i] > dict3[k] and k < len(dict3)-1:
        k += 1
    if dict1[i] == dict2[j] or dict1[i] == dict3[k]:
        output.append(dict1[i])
i=0
j=0
k=0

for j in range(len(dict2)):
    while dict2[j] > dict1[i] and i < len(dict1)-1:
        i += 1
    while dict2[j] > dict3[k] and k < len(dict3)-1:
        k += 1
    if (dict2[j] == dict1[i] or dict2[j] == dict3[k]) and dict2[j] not in output:
        output.append(dict2[j])

pattern = re.compile('[^a-z]')
final_output = sorted(list(set([pattern.sub('', x) for x in output])))

print (final_output)
