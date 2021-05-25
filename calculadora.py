def potencia (a, b):
  pass

def divisao (a, b):
  pass

def mult (a, b):
  return a * b

def sub (a, b):
  return a - b

def soma (a, b):
  return a + b

a = int(input("Digite o primeiro valor"))
b = int(input ("Digite o segundo valor"))

operacao = input("+: Soma\n-: Subtração\n*: Multiplicação\n/: Divisão\n**: Exponenciação")
if operacao == '+':
  resultado = soma(a, b)
elif operacao == '-':
  resultado = sub(a, b)
elif operacao == '*':
  resultado = mult(a, b)
elif operacao == '/':
  resultado = a // b
else:
  resultado = a ** b
print (resultado)