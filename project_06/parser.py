#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" nand2tetris Project 6: Parser Module """


# ---------------- #
# Parser functions #
# ---------------- #

def commandType(command):
    if command[0] == '@':
        return "A_COMMAND"
    elif command[0] == '(':
        return "L_COMMAND"
    else:
        return "C_COMMAND"


def symbol(command):
    ctype = commandType(command)
    if ctype == "A_COMMAND":
        return command[1:]
    elif ctype == "L_COMMAND":
        return command[1:len(command)-1]
    else:
        raise TypeError(
            "The Hack assembly command is neither an A-command nor a L-command")


def dest(command):
    if '=' not in command:
        return "null"
    else:
        return command.split('=')[0]


def comp(command):
    if '=' in command:
        command = command.split('=')[1]
    if ';' not in command:
        return command
    else:
        return command.split(';')[0]


def jump(command):
    if ';' not in command:
        return "null"
    else:
        if '=' in command:
            command = command.split('=')[1]
        return command.split(';')[1]
