# Funções

# Função para escolher tipo de tora
def escolhaTipo():
    # loop para validação
    while True:
        print("Entre com o Tipo de Madeira desejado")
        print("PIN - Tora de Pinho")
        print("PER - Tora de Peroba")
        print("MOG - Tora de Mogno")
        print("IPE - Tora de Ipê")
        print("IMB - Tora de Imbuia")

        tipo = input(">>").upper()

        if tipo == "PIN":
            return 150.40
        elif tipo == "PER":
            return 170.20
        elif tipo == "MOG":
            return 190.90
        elif tipo == "IPE":
            return 210.10
        elif tipo == "IMB":
            return 220.70
        else: #Se não foi nenhum dos tipos acima, opção invalida
            print("Escolha Inválida, entre com o modelo novamente")
            print() #pula linha

# função para quantidade de toras
def qtdToras():
    #loop para validação
    while True:
        try:
            qtd = float(input("Digite a quantidade de toras (m³): "))

            if qtd > 2000:
                print("Não aceitamos pedidos com essa quantidade de toras.")
                print("Por favor, entre com a quantidade novamente.")
                print()
                continue #pula o resto e volta ao inicio do loop

            #Se a quantidade for valida (<= 2000)
            if qtd < 100:
                desconto = 0.0 #0%
            elif qtd < 500:
                desconto = 0.04 #4%
            elif qtd < 1000:
                desconto = 0.09 #9%
            else: # de 1000 a 2000
                desconto = 0.16 #16%

            return qtd,desconto

        except ValueError:
            print("Isso não é um número!")


#função para tipo de transporte

def transporte():
    # loop de validação
    while True:
        print("Escolha o tipo de Transporte:")
        print("1 - Transporte Rodoviário - R$ 1000.00")
        print("2 - Transporte Ferroviário - R$ 2000.00")
        print("3 - Transporte Hidroviário - R$ 2500.00")

        servico = input(">> ")
        print()

        if servico == "1":
            return 1000
        elif servico == "2":
            return 2000
        elif servico == "3":
            return 2500
        else:
            print("Opção inválida. Digite apenas 1, 2 ou 3.")
            print()


# Boas vindas

print("Bem vindo a Madeireira do Lenhador Aluizio Antônio")
print()

# Chamar funções

valorPorM3 = escolhaTipo() #Função para tipo de tora
quantidade, desconto = qtdToras() #Função para quantidade e desconto
valorTransporte = transporte() #Função para selecionar transporte

# Processamento de dados

total = ((valorPorM3 * quantidade) * (1 - desconto)) + valorTransporte

# Saída de dados

print(f"Total: R${total:.2f}")
