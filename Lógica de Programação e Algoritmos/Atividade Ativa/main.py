# Função responsavel por alterar o contato, sendo chamada quando o usuario escolhe a opção 1 na função menu
def cadastrarContato(arrayContatos):

  def existeContato(arrayContatos, telefone): # Função criada pra verificar se o telefone cadastrado é repetido
    if len(arrayContatos) > 0: # Verifica se o array não está vazio
      for contato in arrayContatos:
        if contato["telefone"] == telefone:
          return True
    return False

  while True: # Verificação de telefone já cadastrado
    telefone = input("Digite o telefone do contato: ")
    if not existeContato(arrayContatos, telefone):
      break
    else:
      print("Este telefone já foi cadastrado.\n")
  
  contatoDicionario = { # Dicionario base pra manipulação dos dados
    "nome": input("Digite o nome do contato: "),
    "telefone": telefone,
    "email": input("Digite o e-mail do contato: "),
    "twitter": "@" + input("Digite o twitter do contato: "),
    "instagram": "@" + input("Digite o instagram do contato: ")
  }

  arrayContatos.append(contatoDicionario)
  print("O contato", contatoDicionario["nome"], "foi adicionado com sucesso.\n")

# Função responsavel por alterar o contato, sendo chamada quando o usuario escolhe a opção 2 na função menu
def consultarContato(arrayContatos):
  if len(arrayContatos) > 0: # Verifica se o array não está vazio
    nome = input("Digite o nome do contato a ser consultado: ")
    for contato in arrayContatos: # Percorre todo o array de contatos e retorna o valor pedido na condicional abaixo
      if contato["nome"] == nome:
        print("Nome: " + contato["nome"], "Telefone: " + contato["telefone"], "E-mail: " + contato["email"], "Twitter: " + contato["twitter"], "Instagram: " + contato["instagram"])
        print("==========\n")
        break
      else:
        print("Não existe contato cadastrado com este nome.\n")
  else:
    print("No momento não temos contatos cadastrados.\n")

# Função responsavel por alterar o contato, sendo chamada quando o usuario escolhe a opção 3 na função menu
def removerContato(arrayContatos):
  if len(arrayContatos) > 0: # Verifica se o array não está vazio
    nome = input("Digite o nome do contato a ser removido: ")
    for i, contato in enumerate(arrayContatos): # Percorre todo o array de contatos e retorna o valor pedido na condicional abaixo
      if contato["nome"] == nome:
        print("Contato excluido com sucesso.")
        arrayContatos.pop(i)
        print("==========\n")
        break
      else:
        print("Não existe contato cadastrado com este nome.\n")
  else:
    print("No momento não temos contatos cadastrados.\n")

# Função responsavel por alterar o contato, sendo chamada quando o usuario escolhe a opção 4 na função menu
def alterarContato(arrayContatos):
  if len(arrayContatos) > 0: # Verifica se o array não está vazio
    nome = input("Digite o nome do contato a ser alterado: ")
    for contato in arrayContatos: # Percorre todo o array de contatos e retorna o valor pedido na condicional abaixo
      if contato["nome"] == nome:
        print("Nome: " + contato["nome"], "Telefone: " + contato["telefone"], "E-mail: " + contato["email"], "Twitter: " + contato["twitter"], "Instagram: " + contato["instagram"])
        print("==========\n")
        contato["telefone"] = input("Informe o novo telefone: ")
        contato["email"] = input("Informe o novo email: ")
        contato["twitter"] = input("Informe o novo twitter: ")
        contato["instagram"] = input("Informe o novo instagram: ")
        break
      else:
        print("Não existe contato cadastrado com este nome.\n")
  else:
    print("No momento não temos contatos cadastrados.\n")

# Função responsavel por listar todos os contato, sendo chamada quando o usuario escolhe a opção 5 na função menu
def listarContatos(arrayContatos):
  if len(arrayContatos) > 0: # Verifica se o array não está vazio
    for i, contato in enumerate(arrayContatos): # Percorre todo o array de contatos e retorna o valor pedido na condicional abaixo
      print("Nro {}:".format(i+1))
      print("\tNome: " + contato["nome"], "\tTelefone: " + contato["telefone"], "\tE-mail: " + contato["email"], "\tTwitter: " + contato["twitter"], "\tInstagram: " + contato["instagram"])
      print("==========")
  else:
    print("No momento não temos contatos cadastrados.\n")

# Menu do programa dando escolhas pro usuario e capturando essa escolha atraves da variavel ' menuOpcao '
def menu():
  arrayContatos = [] # Array criado para armazenar todos os contatos cadastrados

  while True: # Menu do programa fica em execução até a opção 0 for escolhida
    print("Seja bem vindo a sua Agenda-Telefônica, digite um dos números abaixo: \n 1- Inserir novo contato \n 2- Fazer consulta por nome \n 3- Remover contato cadastrado \n 4- Alterar contato cadastrado \n 5- Listar todos os contatos cadastrados \n 0- Finalizar")
    menuOpcao = int(input("Aguardando escolha: "))
    if menuOpcao == 1:
      cadastrarContato(arrayContatos)
    elif menuOpcao == 2:
      consultarContato(arrayContatos)
    elif menuOpcao == 3:
      removerContato(arrayContatos)
    elif menuOpcao == 4:
      alterarContato(arrayContatos)
    elif menuOpcao == 5:
      listarContatos(arrayContatos)
    elif menuOpcao == 0:
      print("Encerrando App Agenda-Telefônica...")
      break
    else:
      print("Digite um número válido.\n")

menu() # Chamando a função main do programa