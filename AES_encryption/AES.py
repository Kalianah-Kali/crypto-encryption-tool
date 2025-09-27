#coding:utf-8
def divisible_by_4(variable):

	return variable % 4 == 0
	
def matrix_number(len_matrix):

	if divisible_by_4(len_matrix):
		return len_matrix // 4
	else:
		return len_matrix // 4 + 1
	
def put_into_a_matrix(message) :

	line_nbr = 0
	for x in range(0, len(message), 4):
		line_nbr += 1
	matrix = [[] for x in range(line_nbr)]
	counter = 0
	matrix_counter = 0
	while counter < len(message):
		matrix[matrix_counter] += [bin(ord(message[counter]))] #binary or decimal
		counter += 1
		if (divisible_by_4(counter)):
			matrix_counter += 1
	if len(matrix[len(matrix) - 1]) < 4:
		matrix[len(matrix) - 1] += ['' for x in range(4 - len(matrix[len(matrix) - 1]))]
	if len(matrix) < 4:
		matrix += [['' for x in range(4)] for x in range(4 - len(matrix))]
	if len(matrix) > 4:
		updated_matrix = [[] for x in range(matrix_number(len(matrix)))]
		counter = 0
		c = 0
		while counter < len(matrix):
			updated_matrix[c] += [matrix[counter]]
			counter += 1
			if (divisible_by_4(counter)):
				c += 1
		if len(updated_matrix[len(updated_matrix) - 1]) < 4:
			updated_matrix[len(updated_matrix) - 1] += [['' for x in range(4)] for x in range(4 - len(updated_matrix[len(updated_matrix) - 1]))]
		return updated_matrix
			
	return matrix




print(put_into_a_matrix("hello world!! how"))
print(put_into_a_matrix("tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt"))
