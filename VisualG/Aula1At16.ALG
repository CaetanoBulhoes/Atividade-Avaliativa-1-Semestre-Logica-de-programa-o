Algoritmo "semnome"
//16. Elabore um algoritmo que calcule e mostre a taxa de consumo em km/l que um carro tem
//em um deslocamento. Devem ser criadas variáveis para a distância
//percorrida (em kilômetros), a quantidade de litros consumidos e o valor da taxa
//de consumo (em km/l). O cálculo é feito pela fórmula:
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

escreva("A taxa de consumo de Km/L é:")
escreval(taxadeconsumo)


Fimalgoritmo