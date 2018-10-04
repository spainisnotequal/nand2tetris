#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" nand2tetris Project 6: Assembler """

from sys import argv
import re

from parser import *
from dictionaries import *


if __name__ == "__main__":

    if len(argv) != 2:
        raise TypeError("Invalid number of arguments")
    else:
        ASSEMBLY_FILE = argv[1]

    HACK_FILE = ASSEMBLY_FILE.split('.')[0] + ".hack"

    with open(ASSEMBLY_FILE) as ifile:
        asm_code = ifile.readlines()

    # remove comments
    asm_code = [re.sub(re.compile("//.*?\n"), "", line) for line in asm_code]
    # remove spaces
    asm_code = [re.sub(' +', "", line) for line in asm_code]
    # print(asm_code)
    # remove \n from the end of the line
    asm_code = [line.strip() for line in asm_code]
    # remove blank lines
    asm_code = [line for line in asm_code if line != '']

    with open(HACK_FILE, 'w') as ofile:
        for command in asm_code:
            ctype = commandType(command)
            if ctype == "A_COMMAND":  # @value
                value = symbol(command)
                # "rjust" adds zeros to the right to make a 15 digits number
                binary = '0' + bin(int(value))[2:].rjust(15, '0')
            elif ctype == "C_COMMAND":  # dest=comp;jump
                d = dest(command)
                c = comp(command)
                j = jump(command)
                binary = "111" + COMP[c] + DEST[d] + JUMP[j]
            else:  # ctype == "L_COMMAND":
                print("We are not considering L-intructions yet")

            # write the resulting binary number to the file
            ofile.write(binary + '\n')
