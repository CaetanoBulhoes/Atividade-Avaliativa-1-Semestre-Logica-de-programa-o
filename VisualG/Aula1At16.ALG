Algoritmo "semnome"
//16. Elabore um algoritmo que calcule e mostre a taxa de consumo em km/l que um carro tem
//em um deslocamento. Devem ser criadas vari�veis para a dist�ncia
//percorrida (em kil�metros), a quantidade de litros consumidos e o valor da taxa
//de consumo (em km/l). O c�lculo � feito pela f�rmula:
//taxaDeConsumo = distancia / litros
Var

distancia: real
litros: real
taxadeconsumo: real

Inicio

escreva("Escreva a distancia percorrida(em KM): ")
leia(distancia)
escreval()
escreva("Escreva a quantidade de litros consumida: ")
leia(litros)
escreval()

taxadeconsumo<- distancia / litros

escreva("A taxa de consumo de Km/L �:")
escreval(taxadeconsumo)


Fimalgoritmo