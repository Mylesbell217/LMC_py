#allows command args to be read for file name
import sys

#establishes memory array with 100 0s
mem = [000] * 100

#establishes accumulator as 0 initially
acc = 0

#establishes the next instruction to run
pc = 0

#loads a given program into memory
def loadMem(fileName):
    with open(fileName, "r") as file:
        count = 0
        while count < len(mem):
            line = file.readline()
            print(line.strip())

            if line == "":
                break

            mem[count] = int(line.strip())
            count += 1

#executes a given instruction, by first splitting it down
def execute(instruction: str):
    opcode = instruction[0]
    operand = instruction[1:]

    #matches each opcode to an instruction
    opcode = int(opcode)

    if operand != '':
        data = int(operand)

    global acc
    global pc

    match opcode:
        case 0: #HLT
            return "program end"
        case 1: #ADD
            acc += int(mem[data])
            
            return acc
        case 2: #SUB
            acc -= int(mem[data])
            
            return acc
        case 3: #STA
            mem[data] = acc
            
            return True
        case 5: #LDA
            acc = int(mem[data])
            
            return True
        case 6: #BRA
            pc = data
            return True
        case 7: #BRZ
            if acc == 0:
                pc = data
            return True
        case 8: #BRP
            if acc >= 0:
                pc = data
            return True
        case 9: #INP/OUT
            if operand == "01": #INP
                acc = int(input("input data here: "))
                
            else: #OUT
                print(acc)
                
        case _:
            return "instruction not recognized"

#main program:
if __name__ == "__main__":

    fileName = str(sys.argv[1])

    loadMem(fileName)  #loads the program into the memory list

    running = True
    while running:
        old_pc = pc

        line = execute(str(mem[pc]))
        if line == "program end" or line == "instruction not recognized":
            running = False
        
        if pc == old_pc:
            pc += 1

    print(mem)
    #print(acc)