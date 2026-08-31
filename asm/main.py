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
    file_name = get_file_name()

    #TODO: use the read_file function to pass the file text into decode_line

    #testing reading from file
    #TODO: ensure file name ends in .txt (change to .s later)
    try:
        with open(file_name) as file:
            lex.decode_line(file.readline())
    except FileNotFoundError:
        print("Must be a valid .txt file")


    print(f'execution took {(time.perf_counter() - start_time)} s')