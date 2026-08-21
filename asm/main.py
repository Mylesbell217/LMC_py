#assembler for LMC code
import time
import sys

import lex

#gets the file name to be passed into assembler
#TODO: ensure file name ends in .txt (change to .s later)
def get_file_name() -> str:
    return sys.argv[1]

if __name__ == "__main__":
    timer = time.time()     #times compilation

    #lex.read_file(get_file_name())
    #print(lex.parse_inst("SUB"))
    lex.decode_line("LOOP   LDA A")


    print(f'execution took {(time.time() - timer)*1000} ms')