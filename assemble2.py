import argparse

parser = argparse.ArgumentParser(description='Assembles KEDVAC programs to bytes readable by Logisim')

parser.add_argument('input_file', nargs=1, help='the file to be assembled')
parser.add_argument('-x', action='store_true', help='prepend 0x to every byte')
parser.add_argument('-o', action='store_true', help='outputs the program into Logisim format as output.txt')

args = parser.parse_args()

input_file = args.input_file[0]
prepend = args.x
write_file = args.o

output = []
ops = {'ld': 0, 'sub': 1, 'add': 2, 'st': 3, 'b': 4, 'bneg': 5}

with open(input_file) as f:
    input_data = f.read()
    lines = input_data.split('\n')
    for line in lines:
        if line == 'halt':
            output.append('ff')
        elif line == '':
            output.append('00')
        elif line.find(' ') < 0:
            hex_instruction = "{:02x}".format(int(line))
            output.append(hex_instruction)
        else:
            line_data = line.split(' ')
            op_code = line_data[0]
            address = line_data[1]
            op = ops.get(op_code, None)
            if op == None:
                print 'Unrecognized command \"' + op_code + '\"'
                break
            bin_instruction = "{:03b}{:05b}".format(op, int(address))
            hex_instruction = "{:02x}".format(int(bin_instruction, 2))
            output.append(hex_instruction)
    if write_file:
        f = open('output.txt', 'w')
        f.write('v2.0 raw \n')
        output_str = ''
        for i, instruction in enumerate(output):
            output_str = output_str + instruction + ' '
            if (i+1)%8 == 0:
                output_str = output_str + '\n'

        f.write(output_str)
        f.close()

    else:
        for instruction in output:
            if prepend:
               print '0x',
            print instruction













