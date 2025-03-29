# 16. Escreva um algoritmo que receba 4 números e apresente o somatório deles.    

num_in = int(input("Digite o primeiro número:"))
num_fi = int(input("Digite o ultimo número:"))

soma = 0 

for cont in range(num_in,num_fi + 1):
    cont += 0
    soma += cont

print(f"O somatorio entre esses dois números é: {soma}")