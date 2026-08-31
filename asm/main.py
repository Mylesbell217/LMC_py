#assembler for LMC code
import time
import sys

import lex

#gets the file name to be passed into assembler
def get_file_name():
    return str(sys.argv[1])


if __name__ == "__main__":
    start_time = time.perf_counter()     #compilation timer

    #lex.read_file(get_file_name())
    #print(lex.parse_inst("SUB"))
    #lex.decode_line("LOOP   LDA A")

    #TODO: remove this redundant function, add logic for file name validation
    #TODO: ensure file name ends in .txt (change to .s later)
    file_name = get_file_name()

    #testing reading from file

    try:
        with open(file_name) as file:
            for line in file:
                print(lex.decode_line(line.strip()))
    except FileNotFoundError:
        print("Must be a valid .txt file")


    print(f'execution took {(time.perf_counter() - start_time)} s')