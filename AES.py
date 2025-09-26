#coding:utf-8
def added_4(variable):
	return variable % 4 == 0
	
def matrix_message(message) :
	line_nbr = 0
	for x in range(0, len(message), 4):
		line_nbr += 1
	matrix = [[] for x in range(line_nbr)]
	counter = 0
	matrix_counter = 0
	while counter < len(message):
		matrix[matrix_counter] += [message[counter]]
		counter += 1
		if (added_4(counter)):
			matrix_counter += 1
	if len(matrix[len(matrix) - 1]) < 4:
		matrix[len(matrix) - 1] += ['' for x in range(4 - len(matrix[len(matrix) - 1]))]
	return matrix
print(matrix_message("hello world!!I'll be alive for ever"))
