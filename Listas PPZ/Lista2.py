#1 (triângulo)

l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))

if l1 > (l2+l3) or l2 > (l1+l3) or l3 > (l1+l2):
  print ('Não pode ser um triângulo!')
  
elif l1 == l2 == l3:
  print ('Equilátero')
  
elif l1 == l2 or l1 == l3 or l2 == l3:
  print ('Isósceles')
  
else:
  print ('Escaleno')
  
  
# 2 (Ano Bissexto)

ano = int(input('Digite um ano: '))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print('É ano bissexto.')
else:
    print('Não é ano bissexto.')


# 3


peso = int(input('Quantos kilos: '))

if peso > 50:
  excesso = peso - 50
  multa = excesso * 4
  
else:
  excesso = 'ZERO'
  multa = 'ZERO'
  
  
print ('O excesso de peso foi de', str(excesso),'Kg, portanto a multa foi de R$',str(multa))



# 4 maior número


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo: '))
n3 = int(input('Digite o terceiro: '))

maior = n1

if maior < n2:
  maior = n2
  
if maior < n3:
  maior = n3
  
print ('Maior: %d ' %maior)


# 5 maior e menor número


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo: '))
n3 = int(input('Digite o terceiro: '))

maior = n1
menor = n1

if maior < n2:
  maior = n2
  
if maior < n3:
  maior = n3
  
if menor > n2:
  menor = n2
  
if menor > n3:
  menor = n3
  
print ('Maior: %d ' %maior)
print ('Menor: %d ' %menor)


# 6


valor_hora = float(input('Quanto ganha por hora: '))
horas = int(input('Quantas horas: '))
salario_bruto = valor_hora * horas
im_re = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

print ('Salário Bruto: R$ %.2f' %salario_bruto)
print ('IR : R$ %.2F' %im_re)
print ('INSS : R$ %.2f' %inss)
print ('Sindicato : R$ %.2f' %sindicato)
print ('Salário Líquido: R$ %.2f' %(salario_bruto- im_re -inss - sindicato))


# 7 tintas


tamanho = int(input('Tamanho em metros quadrados: '))
litros = tamanho / 3

if tamanho % 54 == 0:
	latas = tamanho / 54
else: 
	latas = int(tamanho / 54) + 1

preco = latas * 80
print ('%d latas' %latas)
print ('R$ %.2f' %preco)
