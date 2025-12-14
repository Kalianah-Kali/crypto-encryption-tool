#coding:utf-8
def divisible_by_4(variable):

	return variable % 4 == 0
	
def divisible_by_x(number, variable):

	return number % variable == 0
	
def matrix_number(len_matrix):

	if divisible_by_4(len_matrix):
		return len_matrix // 4
	else:
		return len_matrix // 4 + 1
		
def dectobin(integer):
	if integer == '':
		return ''
	string, q = str(integer % 2), integer // 2
	r = q % 2
	while q > 0:
		string += str(r)
		q //= 2
		r = q % 2
	while len(string) < 8:
		string += "0" * (8 - len(string))
	return string[::-1]
	
def bintodec(string):
	if string == '':
		raise ValueError ("value error")
	res, cpt = 0, len(string) - 1
	for x in string:
		res += int(x) * 2**cpt; cpt -=1
	return res
	
def XOR(octet_a, octet_b):
	string = ""
	for x in range(8):
		if octet_a[x] != octet_b[x]:
			string += '1'
		else:
			string += '0'
	return string
	
def put_into_a_matrix(message) :

	line_nbr = 0
	for x in range(0, len(message), 4):
		line_nbr += 1
	matrix = [[] for x in range(line_nbr)]
	counter = 0
	matrix_counter = 0
	while counter < len(message):
		matrix[matrix_counter] += [((message[counter]))] #[dectobin(ord(message[counter]))]
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
	return [matrix]
	
def AddRoundKey(message, key):
	
	matrix_mess = put_into_a_matrix(message)
	while len(key) < len(message):
		key += key
	key = key[0:len(message)]; matrix_key = put_into_a_matrix(key); temp_xor_res = []; xor_res = ''
	for x in range(len(matrix_mess)):
		for y in range(4):
			for z in range(4):
				try:
					temp_xor_res += [[ord(matrix_mess[x][y][z][0]), int(ord(matrix_key[x][y][z]))]]
				except IndexError:
					continue
	for x in temp_xor_res:
		xor_res += chr(bintodec(XOR(dectobin(x[0]), dectobin(x[1]))))
	return xor_res
	
def SubBytes(AddRoundedKey):
	matrixed = put_into_a_matrix(AddRoundedKey)
	for x in matrixed:
		for y in x:
			for z in range(4):
				try:
					print(dectobin(ord(y[z][0])))
				except:
					continue

print(SubBytes(AddRoundKey("KKKKKKK", "hello")))
