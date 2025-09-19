#coding:utf-8
from flask import Flask, render_template, request
import random

def make_it_first(limit):
	number = random.randint(2, limit)
	cp = number - 1
	while cp >= 2:
		if number % cp == 0:
			number = random.randint(2, limit)
			cp = number - 1
		else:
			cp -= 1
	return number

def pgcd(e, phi_n):#with e > phi_n
	list_ = []
	try:
		while e > 0:
			r = e % phi_n
			list_ += [r]
			e = phi_n
			phi_n = r
		return list_[len(list_) - 2]
	except ZeroDivisionError:
		return list_[len(list_) - 2]

def Extended_Euclid(e, phi_n):
	#Euclid's descent
	list_ = []
	while e % phi_n != 0:
		list_ += [[e, phi_n, e // phi_n, e % phi_n]]
		e, phi_n = phi_n, e % phi_n

	if len(list_) < 2:
		return None
	if list_[len(list_) - 1][len(list_[len(list_) - 1]) - 1] != 1:
		return 'the extended Euclid algorithm cannot be applied to these integer!!!'
	#end of Euclid's descent
	#=====================================================================
	#Bezout lift(remontée de Bezout)
	bezout_table, modulo, counter = [], list_[0][0] % list_[1][0], 0
	bezout_table = [[list_[0][0], None, 1, 0], [list_[1][0], None, 0, 1]]
	while modulo != 0:
		q = bezout_table[counter][0] // bezout_table[counter + 1][0]
		r = bezout_table[counter][0] % bezout_table[counter + 1][0]
		bezout_table += [[r, q,
				bezout_table[counter][2] - q * bezout_table[counter+1][2],
				bezout_table[counter][3] - q * bezout_table[counter + 1][3]]]
		counter += 1
		modulo = bezout_table[counter][0] % bezout_table[counter + 1][0]
	u, v = bezout_table[len(bezout_table) - 1][2], bezout_table[len(bezout_table) - 1][3]
	#end of Bezout lift ... With u = d!!!.................................
	return u

def key_generator():
	p, q = make_it_first(255), make_it_first(255)
	n = p * q
	while p == q or n < 255:
		p, q = make_it_first(255), make_it_first(255)
		n = p * q
	phi_n, e = (p - 1) * (q - 1), make_it_first(255)
	while pgcd(e, phi_n) != 1:
		e = make_it_first(255)
	d = Extended_Euclid(e, phi_n)
	if d < 0:
		d = d % phi_n
	return d, n, e, phi_n

def RSA_Protocol_encryptation(SMS, n, e):
	string = ''
	for x in SMS:
		string += chr((ord(x) ** e) % n)
	return string


def RSA_Protocol_decryptation(SMS, private_key, public_key):
	string = ''
	for x in SMS:
		string += chr((ord(x) ** private_key) % public_key)
	return string

app = Flask(__name__, template_folder = 'template')#←,static_folder = 'static'

@app.route('/')
def indexer():
	return render_template('user_choice.html')

@app.route('/shipper_result', methods = ['POST'])
def shipper_result():
	try:
		text_string = request.form.get('text_string')
		if not isinstance(text_string, str) or not text_string.strip():
			return render_template('page_error/error.html')
		try:
			private_key = int(request.form.get('private_key'))
			public_key = int(request.form.get('public_key'))
		except:
			return render_template('page_error/error.html')
		result = RSA_Protocol_decryptation(text_string, private_key, public_key)
		return render_template('server_result.html', result = result)
	except:
		return render_template('page_error/error.html')

@app.route('/recipient_result', methods = ['POST'])
def recipient_result():
	text_string = request.form.get('text_string')
	if not isinstance(text_string, str) or not text_string.strip():
		return render_template('page_error/error.html')
	try:
		public_key = int(request.form.get('public_key'))
		partial_key = int(request.form.get('partial_key'))
	except:
		return render_template('page_error/error.html')
	try:
		result = RSA_Protocol_encryptation(text_string, public_key, partial_key)
		return render_template('recipient_index.html', result = result)
	except:
		return render_template('page_error/error.html')

@app.route('/recipient', methods = ['POST'])
def recipient():
	return render_template('recipient_index.html')

@app.route('/shipper', methods = ['POST'])
def shipper():
	return render_template('server_index.html')

@app.route('/home', methods = ['POST'])
def home():
	return render_template('user_choice.html')

@app.route('/generate_key', methods = ['POST'])
def generate_key():
	return render_template('key_generator.html')

@app.route('/generating', methods = ['POST'])
def generating():
	report = key_generator()
	return render_template('key_generator.html', private_key = report[0], public_key = report[1], partial_key = report[2])

if __name__ == '__main__':
	app.run(debug = True)