# PPZ LISTA 3

#1

n = float(input('Digite um Valor: R$'))

while n < 0 or n >10:
  print ('Valor inválido.')
  n = float(input('Digite outro valor: R$'))


# 2 


usuario = input ('Usuário: ')
senha = input ('Senha: ')

while senha == usuario:
  print ('Senha não pode ser igual ao usuário.')
  usuario = input ('Usuário: ')
  senha = input ('Senha: ')



# 3


a = 80000
b = 200000
ano = 0

while a <= b:
  a += a * 0.03          # x += y   ==  (x = x + y)
  b += b * 0.015
  ano += 1
  
print ('A ultrapassa ou iguala a B em %d anos' %ano)



# 4  finobacci

fibo = [1,1]
i = 0
num = int(input('Entre com um número: '))

while num > len(fibo):
  fibo.append(fibo[i] + fibo[i+1])
  i += 1

print (f'Fibonacci{num}: {fibo[num-1]}')


# 5  Algaritmo de Euclides (MDC)


a = int(input('A: '))
b = int(input('B: '))

while a % b != 0:
  a, b = b, a % b
  
print ('MDC = {}'.format (b))




