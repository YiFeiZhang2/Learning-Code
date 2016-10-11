#checks whether tuple output makes sense
import re

file_name=input("enter file name containing list of tuples\n")
read_file = open(file_name, 'r')
content = re.sub(r'[,\\\s\[\(\)\]\']+', ' ', read_file.read()).strip()
content_list = content.split(' ')
it = iter(content_list)
tuple_list = list(zip(it, it))

num_weird=0
weird_list=list()
print(tuple_list)

for i in range(0, len(tuple_list)-1):
    if tuple_list[i][1] < tuple_list[i+1][0]:
        continue
    if tuple_list[i][1] >= tuple_list[i+1][0]:
        weird_list.append((tuple_list[i], tuple_list[i+1]))

print(num_weird)
