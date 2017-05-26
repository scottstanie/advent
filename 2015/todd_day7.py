import sys
from operator import *

variables = {}

ops = {'AND': and_, 'OR': or_, 'RSHIFT': rshift, 'LSHIFT': lshift, 'NOT': invert}

lines = sys.stdin.readlines()

def translate_symbol(sym):

    sym = variables.get(sym, sym)
    if not isinstance(sym, int):
        try:
            sym = int(sym)
        except:
            return None

    return sym


while True:

    if 'lx' in variables:
        print variables['lx']
        exit(0)

    for line in lines:

        lhs, rhs = line.strip().split(' -> ')
        tokens = lhs.split()

        if len(tokens) == 1:
            try:
                variables[rhs] = int(tokens[0])
            except Exception as e:
                pass

        elif len(tokens) == 2:
            op, operand = tokens
            operand = translate_symbol(operand)
            if operand is None:
                continue

            variables[rhs] = ops[op](operand)

        elif len(tokens) == 3:

            operand1, op, operand2 = tokens

            operand1 = translate_symbol(operand1)
            operand2 = translate_symbol(operand2)

            if operand1 is None or operand2 is None:
                continue

            variables[rhs] = ops[op](operand1, operand2)
