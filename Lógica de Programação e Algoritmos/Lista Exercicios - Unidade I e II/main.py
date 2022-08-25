# I. Conceitos Básicos
# - A)
mostrarDobro = 7 * 2
print(mostrarDobro)

# B)
numeroUm = 5
numeroDois = 7
print(numeroUm + numeroDois, numeroUm - numeroDois, numeroUm * numeroDois, numeroUm / numeroDois)

# C)
idadeEmAnos = 30
print(idadeEmAnos * 365, "dias")

# D)
salarioBruto = 1500
totalVendas = 1000
print(salarioBruto + ((totalVendas * 15) / 100))

# II.Tipos de dados e Variáveis
# 1)
horasTrabalhadas = 40
valorHoraTrabalhada = 10
salBruto = (valorHoraTrabalhada * horasTrabalhadas)
descontoImposto = (salBruto - (salBruto * 18) / 100)
print("O salario bruto é","R$" + str(salBruto), "e o liquido é","R$" + str(descontoImposto))

# 2)
KmPercorridos = 20
litrosParaCompletar = 50
consumoPorKm = (KmPercorridos / litrosParaCompletar)
print(consumoPorKm)

# 3)
a = 777
b = 888
temp = a
a = b
b = temp
print("A:",a,"B:",b)

# 5)
def media():
  numeroUm = int(input("Digite um número: "))
  numeroDois = int(input("Digite outro número: "))
  print((numeroUm + numeroDois) / 2)

# 6)
def saudacao():
  nome = input("Digite seu nome: ")
  print("Olá", nome + ", seja bem-vindo! //", "Seu nome tem " + str(len(nome)) + " letras.")

# 7 e 8)
def condicional():
  numero = int(input("Informe um número: "))
  if numero % 7 == 0:
    print("É multiplo")
  
  if numero > 20:
    print(numero / 2)

# 9)
def emprestimo():
  salario = int(input("Informe seu salário: "))
  valorPrestacao = int(input("Informe o valor da prestação do emprestimo: "))

  if(valorPrestacao > ((salario * 20) / 100)):
    print("Empréstimo não pode ser concedido.")
  else:
    print("Empréstimo pode ser concedido.")

# 10)
def validarCPF():
  cpf = input("Informe o CPF a ser verificado: ")

  if(len(cpf) <= 11):
    print("CPF válido.")
  else:
    print("CPF inválido, contém mais de 11 dígitos.")

# 11)
def salarioOperario():
  horasTrabalhadas = int(input("Informe a quantidade de horas trabalhadas: "))

  if(horasTrabalhadas > 50):
    salarioTotal = 50 * 10
    pagamentoHoraExtra = (horasTrabalhadas - 50) * 20 + salarioTotal
    print("O seu salário final é de:", pagamentoHoraExtra)
  else:
    salarioTotal = horasTrabalhadas * 10
    pagamentoHoraExtra = 0
    print("O seu salário final é de:", salarioTotal)
  
# 12)
def calculadora():
  numeroUm = int(input("Digite um número: "))
  numeroDois = int(input("Digite outro número: "))
  operador = input("Digite um operador aritmético, Ex: -, +, * ou / ")
  
  if(operador == "+"):
    print(numeroUm + numeroDois)
  elif(operador == "-"):
    print(numeroUm - numeroDois)
  elif(operador == "*"):
    print(numeroUm * numeroDois)
  elif(operador == "/"):
    print(numeroUm / numeroDois)