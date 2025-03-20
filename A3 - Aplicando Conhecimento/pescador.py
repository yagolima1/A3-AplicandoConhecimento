'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 

Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos), deve pagar uma multa de R$ 4.00 por quilo excedente, porém toda vez que ele cumpre o estabelecido pelo regulamento de pesca do estado de São Paulo, ele recebe uma bonificação de R$ 1.00 por quilo pescado.

João precisa que você faça um programa, em Python, que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Apresente, na saída de dados, a quantidade de quilos em excesso e o valor da multa, com 2 casas decimais, quando ele infringe o regulamento.

Caso ele atenda o regulamento, apresente, na saída de dados, o valor total da bonificação, com 2 casas decimais).



Entrada
O peso de peixes;

Na entrada, conforme apresentado nos testes abaixo, o programa não deve ter string para emitir mensagem para solicitar ao usuário o valor, portanto utilize apenas o input necessário.

Saída
Na saída, conforme apresentado nos testes abaixo, não deve ter string, para apresentar no valor de saída, apenas  resultado solicitado no enunciado, um em cada linha, formatados com 2 casas decimais.'''

pesoPeixe = float(input())
limite = 50
multaQuilo = 4.0
boniQuilo = 1.0

if pesoPeixe > limite:
    excesso = pesoPeixe - limite
    multa = excesso * multaQuilo
    print(f'{excesso:.2f}')
    print(f'{multa:.2f}')

else:
    boni = pesoPeixe * boniQuilo
    print(f'{boni:.2f}')