import numpy as np
from pprint import pprint


class Node(object):
    def __init__(self, inputs=None, output=None, gate_func=None):
        self.inputs = inputs
        self.output = output
        self.gate_func = gate_func
        self.temp_mark = False
        self.perm_mark = False

    def apply_operators(self):
        '''Runs the gate's function on its inputs, works for all lengths of input'''
        return self.gate_func(*self.inputs)

    def __repr__(self):
        return '[[ %s %s %s, value: %s]]' % (str(self.inputs), self.gate_func or ' -> ', str(self.output), str(self.value))


def visit(node, ordered_nodes, output_to_node):
    '''Topological sort of nodes of a directed graph'''
    if not node or node.temp_mark:
        return
    if not node.perm_mark:
        node.temp_mark = True
        for input_ in node.inputs:
            visit(output_to_node.get(input_), ordered_nodes, output_to_node)
        node.perm_mark = True
        node.temp_mark = False
        ordered_nodes.append(node)


def split_instruction(line):
    input_, output = line.split('->')
    return [input_.strip(' '), output.strip(' ')]


def parse_input(input_):
    if 'OR' in input_:
        left_gate, right_gate = input_.split(' OR ')
        return {'function': np.bitwise_or, 'gates': [left_gate, right_gate]}
    elif 'AND' in input_:
        left_gate, right_gate = input_.split(' AND ')
        return {'function': np.bitwise_and, 'gates': [left_gate, right_gate]}
    elif 'LSHIFT' in input_:
        gate, bits_left = input_.split(' LSHIFT ')

        def new_func(g):
            return np.left_shift(g, int(bits_left))

        return {'function': new_func, 'gates': [gate]}

    elif 'RSHIFT' in input_:
        gate, bits_right = input_.split(' RSHIFT ')

        def new_func(g):
            return np.right_shift(g, int(bits_right))

        return {'function': new_func, 'gates': [gate]}

    elif 'NOT' in input_:
        in_gate = input_.strip('NOT ')
        return {'function': np.invert, 'gates': [in_gate]}
    else:
        return {'function': identity, 'gates': [input_]}


def identity(x):
    return x


def is_int(string):
    try:
        int(string)
    except (ValueError, TypeError):
        return False
    else:
        return True


def main():
    with open('day7.txt', 'rb') as f:
        instructions = f.read().splitlines()

        inputs_to_outputs = []
        output_to_node = {}
        for line in instructions:
            input_, output = split_instruction(line)
            input_dict = parse_input(input_)

            func = input_dict.get('function')
            input_gates = input_dict.get('gates')

            n = Node(input_gates, output, func)

            inputs_to_outputs.append(n)
            output_to_node[output] = n

        ordered_nodes = []
        while inputs_to_outputs:
            node = inputs_to_outputs.pop()
            visit(node, ordered_nodes, output_to_node)

        gate_values = {}
        for node in ordered_nodes:
            if any(not is_int(g) for g in node.inputs):
                node.inputs = [gate_values.get(g) if g in gate_values else int(g) for g in node.inputs]

            value = node.apply_operators()

            gate_values[node.output] = int(value)

        pprint(gate_values)


if __name__ == '__main__':
    main()
