#Boas vindas
print("Bem vindo a Lista de Contatos do Aluizio Antônio")
print() # Pula linha

listaContatos = []
idGlobal = 5498119

# Funções

# Função cadastrar contato
def cadastrarContato(id):
    global listaContatos

    # Formatação do menu de cadastro
    print("-------------------------------------------------")
    print("-------------- MENU CADASTRAR CONTATO -------------")
    print(f"Id do Contato: {id}")
    nome = input("Por favor entre com o nome do Contato: ")
    atividade = input("Por favor entre com a Atividade do contato: ")
    telefone = input("Por favor entre com o telefone do contato: ")


    contato = {
        'id': id,
        'nome': nome,
        'atividade': atividade,
        'telefone': telefone
    }

    listaContatos.append(contato.copy())

    # ajuste formatação
    print("-------------------------------------------------")
    print()


# Função consultar contato

def consultarContatos():
    while True:
        # Formatação do menu
        print("------------ MENU CONSULTAR CONTATOS ------------")
        print("Escolha a opção desejada:")
        print("1 - Consultar Todos os Contatos")
        print("2 - Consultar Contato por id")
        print("3 - Consultar Contato(s) por Atividade")
        print("4 - Retornar")

        opcaoConsulta = input(">> ")
        print()

        # Opção 1: consultar todos
        if opcaoConsulta == "1":
            if not listaContatos:
                print("Nenhum contato cadastrado.")
            else:
                # Formatação de saída
                print("-----------------")
                for contato in listaContatos:
                    print(f"id: {contato['id']}")
                    print(f"nome: {contato['nome']}")
                    print(f"atividade: {contato['atividade']}")
                    print(f"telefone: {contato['telefone']}")
                    print()
                print("-----------------")

        # Opção 2: Consultar por ID
        elif opcaoConsulta == "2":
            try:
                # Formatação do input 
                idBusca = int(input("Digite o id do contato: "))
                print("-----------------")
                encontrado = False
                for contato in listaContatos:
                    if contato['id'] == idBusca:
                        # --- Ajuste de formatação de saída ---
                        print(f"id: {contato['id']}")
                        print(f"nome: {contato['nome']}")
                        print(f"atividade: {contato['atividade']}")
                        print(f"telefone: {contato['telefone']}")
                        encontrado = True
                        break
                if not encontrado:
                    print("Nenhum contato encontrado com esse ID.")
                print("-----------------")
            except ValueError:
                print("ID inválido. Digite um número.")
            print()

        
        # Opção 3: Consultar por Atividade
        elif opcaoConsulta == "3":
            # Formatação do input
            atividadeBusca = input("Digite a Atividade do(s) Contato(s): ")
            print("-----------------")
            encontrado = False
            for contato in listaContatos:
                if contato['atividade'].upper() == atividadeBusca.upper():
                    # Ajuste de formatação de saída
                    print(f"id: {contato['id']}")
                    print(f"nome: {contato['nome']}")
                    print(f"atividade: {contato['atividade']}")
                    print(f"telefone: {contato['telefone']}")
                    print()
                    encontrado = True
            if not encontrado:
                print("Nenhum contato encontrado com essa atividade.")
            print("-----------------")
            print()

        # Opção 4: Retornar
        elif opcaoConsulta == "4":
            break

        else:
            print("Opção inválida. Tente novamente.")
            print()

# Função remover contato

def removerContato():
    global listaContatos

    # Formatação
    print("-------------- MENU REMOVER CONTATO ---------------")

    while True:
        try:
            idRemover = int(input("Digite o id do contato a ser removido: "))

            contatoParaRemover = None
            for contato in listaContatos:
                if contato['id'] == idRemover:
                    contatoParaRemover = contato
                    break
            
            if contatoParaRemover:
                listaContatos.remove(contatoParaRemover)
                print("Contato removido com sucesso!")
                print()
                break # sai do loop de remoção
            else:
                print("Id inválido. Nenhum contato encontrado com esse ID.")
                print()
        
        except ValueError:
            print("Entrada inválida. Digite um número para o ID.")
            print()


# Codigo principal (main)

while True:
    # Formatação do menu
    print("---------------- MENU PRINCIPAL -----------------")
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Contato")
    print("2 - Consultar Contato(s)")
    print("3 - Remover Contato")
    print("4 - Sair")

    opcaoMain = input(">> ")
    print()

    if opcaoMain == "1":
        cadastrarContato(idGlobal)
        idGlobal += 1
    
    elif opcaoMain == "2":
        consultarContatos()

    elif opcaoMain == "3":
        removerContato()

    elif opcaoMain == "4":
        break

    else: 
        print("Opção inválida. Tente novamente.")
        print()
