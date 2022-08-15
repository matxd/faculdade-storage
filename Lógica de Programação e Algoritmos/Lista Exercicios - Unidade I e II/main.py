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
