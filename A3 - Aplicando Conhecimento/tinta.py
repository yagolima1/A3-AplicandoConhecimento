'''Faça um programa, em Python, para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 120.00.

Informe ao usuário a quantidade de tinta a ser comprada e o respectivo  preço.

Leve em consideração que a quantidade de latas a ser comprada deve ser sempre um número inteiro, mesmo que sobre tinta, desta forma será necessário arredondar, para cima, a quantidade de latas calculada.

Apresente, na saída de dados, as informações, exatamente nesta ordem:

- quantidade de latas;

- valor a pagar pela compra das latas, com 2 casas decimais.





Entrada
O tamanho, em metros quadrados, da área a ser pintada - valor numérico real.

Na entrada, conforme apresentado nos testes, o programa não deve ter string para emitir mensagem para solicitar ao usuário o valor, portanto utilize apenas o input necessário.

Saída
- quantidade de latas;

- valor a pagar pela compra das latas, com 2 casas decimais.

Nas saídas, conforme apresentado nos testes, não deve ter string, para apresentar os valores de saída, sendo apenas apresentados nos prints os valores solicitados.'''

import math

area = float(input())

coberturaLitros = 1 / 3
lataTinta = 18
precoLata = 120.00

litrosNecessarios = area * coberturaLitros

latasNecessarias = math.ceil(litrosNecessarios / lataTinta)

valorTotal = latasNecessarias * precoLata

print(latasNecessarias)
print(f'{valorTotal:.2f}')