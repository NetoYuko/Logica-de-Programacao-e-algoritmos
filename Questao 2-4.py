# Boas vindas

print("------ Bem-vindo à Pizzaria do Aluizio Antônio ------")
print("-------------------- CARDÁPIO -----------------------")
print("| Tamanho | Pizza Salgada (PS) | Pizza Doce (PD) |---")
print("|    P    |     R$ 30.00       |     R$ 34.00    |---")
print("|    M    |     R$ 45.00       |     R$ 48.00    |---")
print("|    G    |     R$ 60.00       |     R$ 66.00    |---")
print("-----------------------------------------------------")

# Entrada de dados

totalPedido = 0.0 #variável acumulador

while True:
    # Pede e valida o sabor
    sabor = input("Digite o sabor (PS/PD): ")
    if sabor != "PS" and sabor != "PD":
        print("Sabor Inválido. Tente novamente.")
        print()
        continue #Volta para o início do loop
    
    # Pede e valida o tamanho
    tamanho = input("Digite o tamanho da pizza (P/M/G): ")
    if tamanho != "P" and tamanho != "M" and tamanho != "G":
        print("Tamanho inválido. Tente novamente.")
        print()
        continue

    #Validação SABOR 
    if sabor == "PS":
        if tamanho == "P":
            precoPizza = 30
        elif tamanho == "M":
            precoPizza = 45
        else:
            precoPizza = 60

    elif sabor == "PD":
        if tamanho == "P":
            precoPizza = 34
        elif tamanho == "M":
            precoPizza = 48
        else:
            precoPizza = 66
    
    # formula para somar valor total
    totalPedido += precoPizza
    print(f"Pizza adicionada! subtotal: R${precoPizza:.2f}")
    print()

    # Mais alguma coisa?
    resposta = input("Deseja mais alguma coisa? (S/N): ").upper()
    print()
    if resposta != "S":
        break #Quebra e sai do loop

# Saída de dados

print(f"O valor total a ser pago: R${totalPedido:.2f}")

