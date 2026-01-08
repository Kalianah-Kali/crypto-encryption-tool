#coding:utf-8
from flask import Flask, render_template, request

#coding:utf-8
import time

def afficher(self):
    for x in self:
        time.sleep(0.07)
        print(x, end="")


def convertirUnicode(mot):
    unicode=[]
    for c in mot:
        unicode.append(ord(c))
    return unicode

def dectobin(n):
    resultat = ""
    if n < 2:
        return str(n)
    while n > 0:
        resultat = resultat + str(n%2)
        n = n//2
    return resultat[::-1]

def convertir_binaire(listeU):
    listeB=[dectobin(listeU[x]) for x in range(len(listeU))]
    for x in range(len(listeB)):
        if len(listeB[x]) != 8:
            listeB[x] = "0" * (8- len(listeB[x])) + listeB[x]
    return listeB

def xor(b1,b2):
    if b1==b2 :
        return '1'
    else :
        return '0'

def retrouver(listeb):
    ch=""
    for nb in listeb:
        ch=ch+chr(int(nb,2))
    return ch


def chiffrerXor(mot,cle):
    cbcum = convertir_binaire(convertirUnicode(mot))
    cbcuk = convertir_binaire(convertirUnicode(cle))
    while len(cbcuk) < len(cbcum):
        cbcuk += cbcuk
    cbcuk = cbcuk[0:len(cbcum)]
    liste = []
    res = ""
    for x in range(len(cbcum)):
        for y in range(8):
            fi = xor(cbcum[x][y], cbcuk[x][y])
            res += fi
        liste.append(res)
        res = ""
    return retrouver(liste)

app = Flask(__name__,  template_folder="template")#←,static_folder="static"

@app.route('/')
def indexer():
    return render_template('index.html')


@app.route('/TpyrKc4h', methods=["POST"])
def TpyrKc4h():
    texte = request.form.get('TEXTE')
    key = request.form.get('cle')
    resultat = chiffrerXor(texte, key)
    #return f'{chiffrerXor(texte, key)}'
    return render_template('result.html', message = resultat)

@app.route('/en_d_crypt', methods=["POST"])
def en_d_crypt():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug = True)
