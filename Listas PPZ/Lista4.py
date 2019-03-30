# LISTA 4

# 1

import random

lista = []
maior = 0
menor = 100

for i in range(10):
	n = random.randint(1,100)
	lista.append(n)

	if n < menor: 
		menor = n
	if n > maior:
		maior = n

lista.sort()
print (40*'-')
print (lista)
print ()
print("Menor: {} \nMaior: {}".format (menor, maior))
print (40*'-')



# 2


import random

lista = []
par = []
impar = []

for i in range(20):
	n = random.randint(1,100)
	lista.append(n)

	if n % 2 == 0:
	  par.append (n)
	else:
	  impar.append (n)
	  
lista.sort()
print (40*'-')
print (lista)
print ()
print ('nº pares',par)
print('nº ímpares',impar)
print (40*'-')



# 3


import random

lista1 = []
lista2 = []
lista3 = []

for i in range(10):
	lista1.append(random.randint(1,100))
	lista2.append(random.randint(1,100))
	lista3.append(lista1[i])
	lista3.append(lista2[i])

print (lista1)
print ()
print (lista2)
print ()
print (lista3)



# 4


import re          #retira caracteres específicos

statement = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you"

# Retirando os caracteres especiais
statement = re.sub(u'[,.:]', '', statement)

# Deixando todas as letras minusculas
statement = statement.lower()

# Criando um vetor com todas as palavras dentro de 'statement'
vetor = statement.split()
python = []
count = 0

# Repeticao enquanto o contador 'count' estiver dentro do comprimento da lista de palavras
for count in range (len(vetor)):

	# Variavel com cada palavra do vetor de palavras
	pt = vetor[count]

	# Se a palavra da variavel 'pt' (que muda a cada repeticao) comecar ou terminar com 'python', ela deve ser inserida na lista 'python'
	if pt[0] in "python":
		python.append(pt)
	if pt[-1] in "python":
		python.append(pt)	

print("Lista de palavras:	 ", vetor, "\n \nLista 'python':	 ",python, "\n")



#5



import re

statement = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you"

statement = re.sub(u'[,.:]', '', statement)

statement = statement.lower()

vetor = statement.split()
python = []
count = 0

for count in range (len(vetor)):

	pt = vetor[count]

	if len(pt) >= 4:
		if pt[0] in "python":
			python.append(pt)
		if pt[-1] in "python":
			python.append(pt)	

print("Lista de palavras:	 ", vetor, "\n \nLista 'python':	 ",python, "\n")
