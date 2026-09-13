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


#breaks a line down into pieces
#TODO: finish converting the line into binary equivalent
#use the test file for this, then integrate left hand side tags
def decode_line(line: str):
    parts = line.split(" ")
    parts = list(filter(None, parts)) #removes whitespace

    #filters out the instructions from a line of code
    opcode = parse_inst(parts[0])

    #TODO: recognise that not all instructions have operands (HLT etc)
    data = int(parts[1])
    if data < 10:
        inst = f'{opcode}0{data}'
    else:
        inst = f'{opcode}{data}'
    return inst


#generates label table
def get_labels(buffer: list) -> list:
    labels = []
    for line in buffer:
        words = line.split(" ")
        if words[0] not in instructions:
            labels.append(words[0])
        else:
            print(line)
    return labels
