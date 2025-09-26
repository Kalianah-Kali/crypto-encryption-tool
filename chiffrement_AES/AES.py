#coding:utf-8
def divisible_by_4(variable):

	return variable % 4 == 0
	
def matrix_number(len_matrix):

	if divisible_by_4(len_matrix):
		return (len_matrix // 4)
	else:
		return (len_matrix // 4) + 1
	
def AddRoundKey(message) :

	line_nbr = 0
	for x in range(0, len(message), 4):
		line_nbr += 1
	matrix = [[] for x in range(line_nbr)]
	counter = 0
	matrix_counter = 0
	while counter < len(message):
		matrix[matrix_counter] += [message[counter]]
		counter += 1
		if (divisible_by_4(counter)):
			matrix_counter += 1
	if len(matrix[len(matrix) - 1]) < 4:
		matrix[len(matrix) - 1] += ['' for x in range(4 - len(matrix[len(matrix) - 1]))]
	if len(matrix) > 4:
		updated_matrix = [[] for x in range(matrix_number(len(matrix)))]
		counter = 0
		c = 0
		while counter < len(matrix):
			updated_matrix[c] += [matrix[counter]]
			counter += 1
			if (divisible_by_4(counter)):
				c += 1
				print(c)
		return updated_matrix
		
print(AddRoundKey("Hello World I'm still loving you!!!"))






#print(AddRoundKey("hello world I'm still alive!! a")) #len_matrix = 8
#print(AddRoundKey("hello world I'm still alive!! and I'm still al")) #len_matrix = 12
#print(AddRoundKey("hello world I'm still alive!! and I'")) #len_matrix = 9
#print(AddRoundKey("hello world I'm still alive!")) #len_matrix = 7 **pile
#print(AddRoundKey("hello world I'm still alive!! and I'm still alioo"))
