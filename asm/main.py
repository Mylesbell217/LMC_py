#assembler for LMC code

#Stages:
#1. Preprocess - remove empty lines /
#2. Lex - store labels in list /
#3. Parse - convert each line to binary + match label locations
#4. Gen - write into final output file


import time
import sys

import lex

#gets the file name to be passed into assembler
def get_file_name():
    return str(sys.argv[1])


labels = {}


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
    #print(read_buffer)


    #separates whitespace from each label line
    #TODO: NEEDS TO REMOVE ALL WHITESPACE, THEN RETURN A LIST OF STRINGS FOR EACH INSTRUCTION:
    #E.G. ['start ADD 5', 'SUB 5',......]
    for i in range(len(read_buffer)):
        read_buffer[i] = list(filter(None, read_buffer[i].split(" "))) #removes extra whitespace
        
    #print(read_buffer)

    #extracts labels from the buffer
    #stores in an array as a list with name and address
    for i in range(len(read_buffer)):
        if len(read_buffer[i]) == 3:
            labels[read_buffer[i][0]] = i
            del read_buffer[i][0]
    print(labels)
    #print(read_buffer)
    
    #print(lex.get_labels(read_buffer[0]))

    #parse section:
    for i in range(len(read_buffer)):
        opcode = lex.parse_inst(read_buffer[i][0])
        operand = ""
        if opcode == "0":
            operand = "0"
        elif opcode == "data":
            opcode = ""
            operand = "0" + read_buffer[i][1]
        elif opcode == "901" or opcode == "902":
            operand = ""
        else:
            operand = read_buffer[i][1]

        try:
            if int(operand) < 10:
                print(f'{opcode}0{operand}')
            elif int(operand) >= 10:
                print(f'{opcode}{operand}')
        except ValueError:
            if operand in labels:
                if int(labels[operand]) < 10:
                    print(f'{opcode}0{labels[operand]}')
                else:
                    print(f'{opcode}{labels[operand]}')
            else:
                print("error")

#    #testing reading from file
#    try:
#        with open(file_name) as file:
#            for line in file:
#                print(lex.decode_line(line.strip()))
#    except FileNotFoundError:
#        print("Must be a valid .txt file")


    print(f'execution took {(time.perf_counter() - start_time)} s')