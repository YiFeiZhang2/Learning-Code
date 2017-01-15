import os
import re

dir = "/Users/yili/Documents/Richard USB info/Learning-Code/Python/english-words-master/"
file_name="word_dict.txt"

f = open(os.path.join(dir, file_name), 'r')

txt = f.read()

for ch in ['[', ']', '\'', ']', ',']:
    if ch in txt:
        txt = txt.replace (ch, "")

if ' ' in txt:
    txt = txt.replace (' ', '\n')

print (txt)
