#TODO:
#read each line of code (store in linkedlist??)
#break down into opcode, operand
#rewrite as binary equivalent
#save to new file

instructions = {
    "HLT": 0,
    "ADD": 1,
    "SUB": 2,
    "STA": 3,
    "LDA": 5,
    "BRA": 6,
    "BRZ": 7,
    "BRP": 8,
    "INP": 9,
    "OUT": 9
}


#matches a given instruction with its opcode
def parse_inst(inst: str) -> str:
    """ matches a given instruction with its opcode """

    match inst:
        case "HLT":
            return "0"
        case "ADD":
            return "1"
        case "SUB":
            return "2"
        case "STA":
            return "3"
        case "LDA":
            return "5"
        case "BRA":
            return "6"
        case "BRZ":
            return "7"
        case "BRP":
            return "8"
        case "INP" | "OUT":
            return "9"
        case "DAT":
            return "data"
        case _:
            return "Error"


#reads a given file
def read_file(fileName: str):
    with open(fileName, 'r') as file:
        print(file.readlines())


#breaks a line down into pieces
#TODO: finish converting the line into binary equivalent
#use the test file for this, then integrate left hand side tags
def decode_line(line: str):
    parts = line.split(" ")
    parts = list(filter(None, parts)) #removes whitespace

    print(parts)
    print(len(parts))

    #filters out the instructions from a line of code
    for item in parts:
        if item in instructions:
            print(item)
        else:
            print("identifier")
