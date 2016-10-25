#!/usr/local/bin/python3
import os
import re
import copy

#returns list of files in directory
def file_list_maker(dir, name):
    output_list = list()
    for filename in os.listdir(path=dir):
        if filename.endswith(name+".sv.vcf"):
            output_list.append(filename)
    return output_list

#returns sorted 3D list from list of files
#the order of the list of files is the same as the order of the list of files
#list of fields -> list of lines -> list of files
#*args is a list of applicable file names
def file_list_reader(file_list):
    output_list = []
    for file_name in file_list:
        read_file = open(file_name, 'r')
        file = [line.split('\t') for line in read_file]
        file.sort(key = lambda x: (conv_int(x[1])))
        output_list.append(file)
        read_file.close()
    return output_list

#returns list of indexes of mut_list (mut_list[index]) that are the cancer samples
def cancer_ind_list_creater(file_list, *args):
    cancer_ind_list = [int(file_list.index(cancer_file)) for cancer_file in args]
    return cancer_ind_list

#creates list of 0s
def zero_list_maker(n):
    zero_list = [0] * n
    return zero_list

#try to read an int
def conv_int(n):
    try:
        return int(n)
    except ValueError:
        return 0

#find starting position
def staFinder(mut_list, sample_index, line_ind):
    return conv_int(mut_list[sample_index][line_ind][1])

#find min position
def endFinder(mut_list, sample_index, line_ind):
    return (conv_int(mut_list[sample_index][line_ind][1])+(-1)*conv_int(mut_list[sample_index][line_ind][10]))

#returns true if items in one list are smaller than items in another list at all each corresponding index
def within(list1, max_list):
    if len(list1) != len(max_list):
        return False
    for i in range(len(max_list)):
        if list1[i] > max_list[1]:
            return False
    return True

#Compare Start and End positions of cancer samples for overlap
#Overlap is found when the max start pos across all cancer samples at their current position is smaller than the min end position
def shared_mutation(mut_list, mut_type, cancer_ind_list):
    num_cancer = len(cancer_ind_list)
	
    max_line = [len(mut_list[i]) for i in cancer_ind_list]
    line_tracker = [0]*num_cancer
    tuple_list = list()	

    while within(line_tracker, max_line):
        try:
            start_pos=[staFinder(mut_list, cancer_ind_list[m], line_tracker[m]) for m in range(num_cancer)]
            end_pos=[endFinder(mut_list, cancer_ind_list[n], line_tracker[n]) for n in range(num_cancer)]
            max_S = max(start_pos)
            ind_S = start_pos.index(max_S)
            min_E = min(end_pos)
            ind_E = end_pos.index(min_E)
        except IndexError as e:
            break

        if max_S <= min_E:
            tuple_list.append((max_S, min_E))
            line_tracker[ind_E] += 1 
        else:
            line_tracker[ind_E] += 1

    return tuple_list

#the list of tuples may contain overlaps between tuples
#tuple_trim merges those overlaps
def trim_overlap(tuple_list):
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
    return tuple_list

#remove indexes in the list of tuples where SV have already been seen at the positions
def trim_seen(tuple_list, mut_list, cancer_ind_list):
    for i in range(len(mut_list)):
        if any(i == x for x in cancer_ind_list):
            continue
        else:
            for line_ind in range(len(mut_list[i])):
                start_pos = conv_int(mut_list[i][line_ind][1])
                end_pos = conv_int(mut_list[i][line_ind][1])+(-1)*conv_int(mut_list[i][line_ind][10])
                for SEpair in tuple_list:
                    if (start_pos >= SEpair[0] and start_pos <= SEpair[1]) or (end_pos >= SEpair[0] and end_pos <= SEpair[1]) or (start_pos < SEpair[0] and end_pos > SEpair[1]):
                        tuple_list.pop(tuple_list.index(SEpair))
    return tuple_list



#takes trimmed tuple_list and matches the cancer files for SV positions that fall within the start/end pairs
def print_output(mut_list, mut_type, tuple_list, cancer_ind_list, *cancer_files):
    file_name = "whilms_sv_chr17_"+mut_type+"_v2.sv.vcf"
        #opens new file in the whilms_mutation folder
    final_file = open(os.path.join("/Users/yili/Desktop/novo/whilms_mutation_v2", file_name), 'w')

    formatted_file_list = [X.replace("_chr17_clear_"+mut_type+".sv.vcf", "") for X in cancer_files]
        #print(formatted_file_list)
    header = "CHROM\tSTARTPOS\tENDPOS\tTOTLEN\tID\tREF\tALT\tSVTYPE\tQUAL\tFILTER\tQGAP\tMINMAPQ\tMINSC\tMINTIPQ\t" + "\t".join(formatted_file_list)
        #print(header)
	
    final_file.write(header+"\n")
    
    for SEpair in tuple_list:
        curr_line = [0]*14
        for sample in mut_list:
            if (mut_list.index(sample) not in cancer_ind_list):
                continue
            else:
                for line in sample:
                    start_pos = conv_int(line[1])
                    end_pos = conv_int(line[1]) + (-1)*conv_int(line[10])
                    if (start_pos >= SEpair[0] and start_pos <= SEpair[1]) or (end_pos >= SEpair[0] and end_pos <= SEpair[1]) or (start_pos < SEpair[0] and end_pos > SEpair[1]):
                        curr_line[0] = "chr17"
                        curr_line[1] = SEpair[0]
                        curr_line[2] = SEpair[1]
                        curr_line.append(str(start_pos) + ":" + str(end_pos))
        final_file.write(("\t").join(map(str, curr_line))+"\n")

    final_file.close()
    return final_file


working_dir = input("Enter Working Directory: ")
working_dir = "/Users/yili/Desktop/novo"
mut_type = "comp"
cancer_files = input("Enter Files From Cancer Samples, Seperated By Space: ").split(" ")
cancer_files = ["869_EC0067_chr17_clear_"+mut_type+".sv.vcf", "869_EC0068_chr17_clear_"+mut_type+".sv.vcf"]

file_list = file_list_maker(working_dir, mut_type)
mut_list = file_list_reader(file_list)
cancer_ind_list = cancer_ind_list_creater(file_list, *cancer_files)
tuple_list = shared_mutation(mut_list, mut_type, cancer_ind_list)
tuple_trim = trim_seen(trim_overlap(tuple_list), mut_list, cancer_ind_list)
print(tuple_trim)
print_output(mut_list, mut_type, tuple_trim, cancer_ind_list, *cancer_files)
