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

# III. Entrada e Saida
# 5)
def media():
  numeroUm = int(input("Digite um número: "))
  numeroDois = int(input("Digite outro número: "))
  print((numeroUm + numeroDois) / 2)

# 6)
def saudacao():
  nome = input("Digite seu nome: ")
  print("Olá", nome + ", seja bem-vindo! //", "Seu nome tem " + str(len(nome)) + " letras.")

# IV. Condicional IF
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
  
# V. Condicional IF (Estrutura Aninhada)
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

# 13)
def classeEleitoral():
  idade = int(input("Digite sua idade: "))
  if(idade < 16):
    print("Não-eleitor")
  elif(idade >= 18 and idade <= 65):
    print("Eleitor obrigatório")
  elif(idade >= 16 and idade < 18 or idade > 65):
    print("Eleitor facultativo")

# 14)
def siglaEstado():
  userEstado = input("Digite a sigla do seu Estado: ").upper()
  if(userEstado == "RJ"):
    print("Carioca")
  elif(userEstado == "SP"):
    print("Paulista")
  elif(userEstado == "MG"):
    print("Mineiro")
  else:
    print("Outros estados")

# 15)
def precoFruta():
  frutasQts = int(input("Digite a quantidade de Maçãs compradas: "))
  if(frutasQts < 12):
    print(frutasQts * 0.30)
  elif(frutasQts >= 12):
    print(frutasQts * 0.25)

# 16)
def triangulo(a, b, c):
  if(a == b and b == c):
    print("Triângulo Equilátero")
  elif(a == b or b == c or c == a):
    print("Triângulo Isósceles")
  else:
    print("Triângulo Escaleno")

# 17)
def sistemaEscolar(nome, nota1, nota2, nota3, nota4):
  media = (nota1 + nota2 + nota3 + nota4) / 4
  if(media >= 6):
    print(nome + ", você está aprovado")
  elif(media < 5):
    print(nome + ", você está automaticamente reprovado")
  elif(media < 6 and media > 5):
    exameFinal = float(input("Informe a nota do seu Exame Final: "))
    mediaFinal = (media + exameFinal) / 2
    if(mediaFinal >= 6):
      print(nome + ", você está aprovado")
    else:
      print(nome + ", você está reprovado")