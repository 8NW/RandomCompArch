import argparse

parser = argparse.ArgumentParser(description='Assembles KEDVAC programs to bytes readable by Logisim')

parser.add_argument('input_file', nargs=1, help='')
parser.add_argument('-x', help='prepend 0x to', action='store_true')

args = parser.parse_args()

input_file = args.input_file[0]

with open(input_file) as f:
	input_data = f.read()
	data_string_array = input_data.split('\n')

	data_hex_array = []

	for string in data_string_array:
		data_string_content = data_string_array.split(' ')
			data_hex_string = ''

			if data_string_array[0] == 'ld':
				bin_op.bin(0).split(b)
				bin_index = str(bin(int(data_string_array[1]))).split(b)
				temp_string = ''
				data_hex_string.append(hex(temp_tring.append(bin_op[1]).append(bin_index[1])))

			elif data_string_array[0] == 'sub':
				bin_op.bin(1).split(b)
				bin_index = str(bin(int(data_string_array[1]))).split(b)
				temp_string = ''
				data_hex_string.append(hex(temp_tring.append(bin_op[1]).append(bin_index[1])))

			elif data_string_array[0] == 'add':
				bin_op.bin(2).split(b)
				bin_index = str(bin(int(data_string_array[1]))).split(b)
				temp_string = ''
				data_hex_string.append(hex(temp_tring.append(bin_op[1]).append(bin_index[1])))

			elif data_string_array[0] == 'st':
				bin_op.bin(3).split(b)
				bin_index = str(bin(int(data_string_array[1]))).split(b)
				temp_string = ''
				data_hex_string.append(hex(temp_tring.append(bin_op[1]).append(bin_index[1])))

			elif data_string_array[0] == 'b':
				bin_op.bin(4).split(b)
				bin_index = str(bin(int(data_string_array[1]))).split(b)
				temp_string = ''
				data_hex_string.append(hex(temp_tring.append(bin_op[1]).append(bin_index[1])))

			elif data_string_array[0] == 'bneg':
				bin_op.bin(5).split(b)
				bin_index = str(bin(int(data_string_array[1]))).split(b)
				temp_string = ''
				data_hex_string.append(hex(temp_tring.append(bin_op[1]).append(bin_index[1])))

			elif data_string_array[0] == 'halt':
				bin_op.bin(7).split(b)
				bin_index = str(bin(int(data_string_array[1]))).split(b)
				temp_string = ''
				data_hex_string.append(hex(temp_tring.append(bin_op[1]).append(bin_index[1])))	

			else:
				bin_index = bin(data_string_array[1]).split(b)
				temp_string = ''
				data_hex_string.append(hex(temp_tring.append(bin_index[1])))

			data_string_array.append(data_hex_string)



				


	print input_data

