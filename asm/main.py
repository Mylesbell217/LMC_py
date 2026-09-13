#assembler for LMC code

#Stages:
#1. Preprocess - remove empty lines
#2. Lex - store labels in list
#3. Parse - convert each line to binary + match label locations
#4. Gen - write into final output file


import time
import sys

import lex

#gets the file name to be passed into assembler
def get_file_name():
    print(str(sys.argv[1]))
    return str(sys.argv[1])


if __name__ == "__main__":
    start_time = time.perf_counter()     #compilation timer

    #TODO: remove this redundant function, add logic for file name validation
    #TODO: ensure file name ends in .txt (change to .s later)
    file_name = get_file_name()

    #Preprocessing:
    read_buffer = []    #buffer to hold file contents during compilation process
    with open(file_name) as file:
        for line in file:
            if line != '\n':
                read_buffer.append(line.strip())

    print(read_buffer)

    print(list(filter(None, read_buffer[0].split(" ")))) #removes extra whitespace
    

    print(lex.get_labels(read_buffer))

    #symbol match test
    for i in range(len(read_buffer)):
        line = read_buffer[i]
        read_buffer[i] = lex.decode_line(line.strip())
    print(read_buffer)


#    #testing reading from file
#    try:
#        with open(file_name) as file:
#            for line in file:
#                print(lex.decode_line(line.strip()))
#    except FileNotFoundError:
#        print("Must be a valid .txt file")


    print(f'execution took {(time.perf_counter() - start_time)} s')