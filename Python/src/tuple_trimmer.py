#finds any overlap in tuples, and joins them together
import re
import copy

file_name = input("enter file name containing list of tuples\n")
read_file = open(file_name, 'r')
content = re.sub(r'[,\\\s\[\(\)\]\']+', ' ', read_file.read()).strip()
content_list = [int(x) for x in content.split(' ')]
it = iter(content_list)
tuple_list = list(zip(it, it))

#print(tuple_list)
ori_length = len(tuple_list)

ind = 0
while ind < len(tuple_list)-1:
    if tuple_list[ind][1] < tuple_list[ind+1][0]:
        ind += 1
        continue
    elif tuple_list[ind][1] >= tuple_list[ind+1][0]:
        new_tuple = (tuple_list[ind][0], tuple_list[ind+1][1])
        tuple_list[ind] = new_tuple
        prev = copy.deepcopy(tuple_list[:ind+1])
        next = copy.deepcopy(tuple_list[ind+2:])
        tuple_list = prev + next
print(ori_length - len(tuple_list))
print(tuple_list)
