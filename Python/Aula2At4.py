# 4. Faça um programa que leia dois valores para as variáveis A e B e efetue a troca dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A Apresente os valores trocados.

num1 = float(input("Digite um número:"))
num2 = float (input("Digite outro número:"))

t1 = num2
t2 = num1 

print(f"Número A:{num1} e o número B:{num2}\nTrocando fica A:{t1} e B:{t2}")