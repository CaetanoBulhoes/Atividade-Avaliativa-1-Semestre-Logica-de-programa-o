#13. Escreva um programa que receba um número e escreva na tela a tabuada de multiplicação dele.

num = int(input("Digite um número:"))

for cont in range (1,11):
    multi = num * cont
    print(f"{num} X {cont} = {multi}")
