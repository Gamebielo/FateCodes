#Python para zumbis, lista 1

#1

print ('Vamos fazer uma soma!')
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
r = n1+n2
print ('A soma de {} com {} resultou em {}'.format (n1,n2,r))

#2

print ('Vamos converter metros em milímetros!')
a = int(input('Digite um valor):'))
m = (a)*1000
print ('Esse valor em milímetros é igual a:',m)

#3

print ('Vamos converter tudo para segundos!')
d = int(input('Digite uma quantidade de dias:'))
h = int(input('Digite uma quantidade de horas:'))
m = int(input('Digite uma quantidade de minutos:'))
s = int (input('Digite uma quantidade de segundos:'))

totalsegundos = (d*24*60*60)+(h*60*60)+(m*60)+s

print (d,"dias",h,"horas",m,"minutos",s,"segundos representam", totalsegundos,"segundos")


#4 aumento de salário

salario = int(input('Qual é o valor do salário? '))
perc = int(input('Qual é a porcentagem de aumento? '))
print (salario+(salario*perc/100))

#5

preco = int(input('Qual é o preço da mercadoria? \n'))
perc = int(input('Qual é o percentual de desconto? \n'))
novopreco = (preco-(preco*perc/100))
desconto = (preco-novopreco)
print (f'O desconto foi de R$:{desconto:.2f}')
print (f'O preço a pagar é de R${novopreco:.2f}')

#6

dist = float(input('Digite a distância em Km:'))
vm = float(input('Digite a velocidade média:'))
tempo = dist/vm
print ('Tempo em horas %.1f' %tempo)

#7 converter C° em F°

c = int(input("Digite a temperatua em Celsius: "))
f = float(9*c/5) + 32

print ('%d Fahrenheit' %f)

#8 de F° para C°

f = float(input('Digite uma temperatura em Fahrenheit:'))
c = float(f-32)/1.8
print ('%d Celsius' %c)

#9

kmp = int(input('Digite a quantidade de km percorridos:'))
dias = int(input('Digite a quantidade de dias:'))

print ('Valor do aluguel: R$ %.2f' %(kmp*0.15+dias*60))

#10

qntCigarros = int(input('Quantos cigarros por dia:'))
anosFumando = int(input('Anos fumando:'))

totalCigarros = (anosFumando*365)*qntCigarros
diasPerdidos = (totalCigarros*10)/24

print ('Dias perdidos %d' %diasPerdidos)

#11

print ('2 elevado a 1 milhão tem %d digitos' %len(str(2**1000000)))
