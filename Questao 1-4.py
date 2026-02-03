# Boas vindas
print("Bem vindo ao sistema do Aluizio Antônio")

# Entradas de dados

valorBase = float(input("Informe o valor Base do plano: "))
idade = int(input("Informe a idade do cliente: "))

# teste logico 

if idade >= 0 and idade < 19: # (0 a 18 anos)
    multiplicador = 1.0 # 100 / 100
elif idade >= 19 and idade < 29: # (19 a 28 anos)
    multiplicador = 1.5 # 150 / 100
elif idade >= 29 and idade < 39: # (29 a 38 anos)
    multiplicador = 2.25 # 225 / 100
elif idade >= 39 and idade < 49: # (39 a 48 anos)
    multiplicador = 2.40 # 240 / 100
elif idade >= 49 and idade < 59: # (49 a 58 anos)
    multiplicador = 3.50 # 350 / 100
else: # (>= 59 anos)
    multiplicador = 6.0 # 600 / 100

# Processamento dos dados

valorMensal = valorBase * multiplicador

# Saída de dados
print(f"O valor mensal do plano é de: R${valorMensal:.2f}")