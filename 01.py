# -*- coding: utf-8 -*-
"""01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/leobezerra/python-zero/blob/master/01.ipynb

# Primeiros passos

O interpretador Python é um cara legal que gosta de conversar, mas ele é um pouco repetitivo..

Os notebooks Jupyter se comunicam com o interpretador, mandando suas mensagens e mostrando as resposta que ele dá. 

Clique no botão de Play para executar a célula abaixo (ou selecione a célula e aperte Shift+Enter).
"""

"Oi Python!"

"""## Melhorando a conversa com o interpretador

>Se o interpretador apenas repete o que eu falo, pra que ele serve? 🤔
>*, perguntou um aluno apressado.*

O interpretador é mais sagaz do que parece. Teste as células abaixo:
"""

"Oi Python!".upper()

"Oi Python!".lower()

"Oi Python!" + " Tudo bom?"

"Oi Python!".split()

"""### Exercícios de fixação

EF1 - Peça pra o interpretador dizer **"Bom dia"** com letras minúsculas.
"""

"Bom dia".upper()

"""EF2 - Peça pra o interpretador dizer **"Boa tarde"** com letras maiúsculas."""

"Boa tarde".upper()

"""EF3 - Peça pra o interpretador dizer **"Bom dia ou Boa tarde?"**, sendo o **"Bom dia"** com letras maiúsculas e o **"boa tarde"** com letras minúsculas."""

"Bom dia".upper() + " ou " + "Boa tarde".lower()

"""### Exercícios complementares

EC1 - O que você acha que a opção `split()` significa para o interpretador? Dica -- pesquise no Google Translate.

```
# This is formatted as code
```

*Escreva sua resposta aqui*

A gente vai estudar o `split` com mais calma depois, mas por enquanto vamos ver um pouco sobre números.

## Trabalhando com números

O interpretador Python também consegue lidar com números e operadores aritméticos, que podem ser usados para construir **expressões aritméticas**. 

As regras básicas sobre expressões aritméticas em Python são:

* Em geral, a precedência dos operadores em Python segue a precedência que conhecemos da matemática. 
* Assim como na matemática, é possível usar parênteses para mudar a ordem de avaliação de uma expressão.
* Caso reste apenas operações de mesma precedência, a expressão passa a ser avaliada da esquerda para a direita.

Alguns dos operadores aritméticos disponíveis em Python estão listados abaixo.

| Símbolo | Operação |
|:----:|---|
| +  | Adição |
| -  | Subtração |
| /  | Divisão |
| // | Divisão inteira |
| %  | Resto |
| *  | Multiplicação |
| **  | Exponenciação |

Teste as células abaixo:
"""

1+2+5

2-1

1*2

3/4

2 ** 3

"""No entanto, você não deve misturar textos e números:"""

"Este é um texto" + 3

"""### Exercícios de fixação

EF4 - Calcule o produto dos números 11 e 12.
"""

11 * 12

"""EF5 - Calcule o quadrado do número 16."""

16 ** 2

"""EF6 - Calcule a raiz quadrada de 1024."""

1024 ** 1 // 2

"""### Exercícios complementares

Os operadores // e % trabalham com divisão inteira. Por exemplo, dividir 15 por 10 considerando apenas número inteiros é igual a 1. O resto da divisão é igual a 15 - (10*1), ou seja, 5.
"""

15//10

15%10

"""EC2 - Calcule o resto da divisão de 227 por 20."""



"""# Valores, nomes e variáveis

Em Python, tanto textos como números são chamados de *valores*. 

Podemos nos referir a valores usando *nomes*. 

>Em outras linguagens, usa-se o termo **variável** em vez de nome. Vamos adotar este termo aqui por ele ser mais universal.

Teste as células abaixo:
"""

x = 2          # qualquer coisa após o # é um comentário
y = 5
x + y

"""Múltiplas variáveis podem estar associadas ao mesmo valor."""

x = y = 1
y

texto = 'Este é um texto.' # textos podem ser escritos entre aspas simples
texto

outro_texto = "Este é outro texto." # textos podem ser escritos entre aspas duplas
outro_texto

"""### Exercícios de fixação

Para verificar que seu código está correto, lembre-se de acrescentar uma linha contendo apenas o nome da variável para visualizar o valor associado a ela.

EF7 - Associe uma variável `numero` ao número `10`.
"""



"""EF8 - Associe uma variável `nome` ao texto `Python`."""



"""EF9 - Associe uma variável `resto` ao resultado do operação de resto entre `234` e `10`."""



"""EF10 - Associe uma variável `k` ao valor `8`. Associe uma variável `quadrado_k` ao quadrado do valor associado à variável `k`."""



"""EF11 - Associe uma váriavel `z` ao valor `256`. Associe uma variável `divisao_zk` ao resultado da divisão entre os valores associados às variáveis `z` e `k`."""



"""## Dados informados pelo usuário

O procedimento `input()` solicita ao usuário dados que podem ser associados a variáveis. É possível personalizar a mensagem de solicitação, como mostrado abaixo.
"""

texto_usuario =  input("Diga um valor: ")
texto_usuario

"""Por padrão, qualquer dado passada pelo usuário será tratado como texto. Para tratá-lo como um valor numérico, você deve usar os procedimentos `int()` ou `float()`, dependendo de serem números inteiros ou reais."""

inteiro = int(input("Diga um valor inteiro: "))
inteiro + 1

real = float(input("Diga um valor real: "))
real + 1

"""### Exercícios de fixação

EF12 - Solicite ao usuário *seu nome* e o associe a uma variavél chamada `nome`.
"""



"""EF13 - Solicite ao usuário *sua idade* e a associe a uma variável chamada `idade`."""



"""EF14 - Solicite ao usuário *sua altura* e a associe a uma variável chamada `altura`."""



"""## Informando dados ao usuário

Assim como é possível receber dados do usuário, também é possível informar dados ao usuário.

Para isto, usamos o procedimento `print()`.
"""

print(texto)

"""É possível informar os valores associados a múltiplas variáveis com uma única chamada ao procedimento `print()`."""

print(texto, x)

"""Também é possível informar textos, valores e o resultado de expressões:"""

print("Testando", 3, x + y)

"""### Exercícios de fixação

EF15 - Informe ao usuário **seu nome**.
"""



"""EF16 - Informe ao usuário **sua idade**."""



"""EF17 - Informe ao usuário **seu índice de massa corporal (IMC)**. Para isso, solicite ao usuário seu peso."""



"""## Exercícios do URI

O URI é um juiz online utilizado em treinamentos para competições de programação.

Nesta disciplina, utilizaremos exercícios inspirados na seção **Iniciante**, adaptados para o nosso contexto.

Para ver a descrição do exercício em sua versão original do URI, clique no seu número.

[1008](https://www.urionlinejudge.com.br/judge/pt/problems/view/1008) - Um sistema do setor de recursos humanos de uma empresa deve calcular o salário a ser pago para cada funcionário da empresa em função de quantas horas o funcionário trabalhou no mês e de quanto ele recebe por hora trabalhada.

Escreva um código Python que leia o nome de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula seu salário. Em seguida, mostre o nome e o salário do funcionário.

|.| Entrada | Saída |
|-|----|---|
| *Exemplo 1* | João 100 5.50  | João 550.00 | 
| *Exemplo 2* | Maria 200 20.50 | Maria 4100.00 |
| *Exemplo 3* | Facebookson 145 15.55 | Facebookson 2254.75 |
"""

nome = None
salario = None
horas_trab = None

nome = input()
salario = float(input())
horas_trab = float(input())

print(str(nome) + " " + str(salario * horas_trab))

"""[1009](https://www.urionlinejudge.com.br/judge/pt/problems/view/1009) - No caso de empresas do setor de comércio, a remuneração mensal de cada vendedor é composta por um salário fixo mais uma bonificação proporcional às vendas efetuadas pelo vendedor naquele mês.

Escreva um código Python que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informe o total que ele deverá receber no final do mês.

|.| Entrada | Saída |
|-|----|---|
| *Exemplo 1* | João 500 1230.30  | João 684.54 | 
| *Exemplo 2* | Pedro 700 0.00 | Pedro 700.00 |
| *Exemplo 3* | Mangojata 1700 1230.50 | Mangojata 1884.58 |
"""

nome = None
salario = None
comissao = 0.15
vendas = None

nome = input()
vendas = int(input())
salario = float(input())

vendas_comissao = vendas * comissao (CONTINUA DAQUI)

print(str(nome) + " " + str()

"""[1010](https://www.urionlinejudge.com.br/judge/pt/problems/view/1010) - Outro tipo de sistema utilizado no setor de comércio é o sistema de frente de loja, que calcula o total de uma venda baseado nos itens adquiridos, suas quantidades e seus valores unitários.

Escreva um código Python que leia as informações de dois produtos adquiridos em uma compra e informe o valor a ser pago. Para cada produto, leia seu código, sua quantidade e seu valor unitário.

|.| Entrada | Saída |
|-|----|---|
| *Exemplo 1* | 12 1 5.30 <br> 16 2 5.10 | VALOR A PAGAR: 15.50 |
| *Exemplo 2* | 13 2 15.30 <br> 161 4 5.20 | VALOR A PAGAR: 51.40 |
| *Exemplo 3* | 1 1 15.10 <br> 2 1 15.10 | VALOR A PAGAR: 30.20 |
"""



"""[1018](https://www.urionlinejudge.com.br/judge/pt/problems/view/1018) - Sistemas de frente de loja também devem auxiliar vendedores a dar trocos. Por simplicidade, vamos considerar primeiro apenas trocos inteiros, que podem ser dados usando apenas cédulas.

Escreva um código Python que leia um valor de troco e informe quantas cédulas de cada valor devem ser entregues pelo vendedor ao cliente.

**Obs.:** Considere que ainda existem notas de R$ 1,00.

|.| Entrada | Saída |
|-|----|---|
| *Exemplo 1* | 576 | 5 nota(s) de 100,00 <br /> 1 nota(s) de 50,00 <br /> 1 nota(s) de 20,00 <br /> 0 nota(s) de 10,00 <br /> 1 nota(s) de 5,00  <br /> 0 nota(s) de 2,00  <br /> 1 nota(s) de 1,00 |
| *Exemplo 2* | 11257 | 112 nota(s) de 100,00 <br /> 1 nota(s) de 50,00 <br /> 0 nota(s) de 20,00 <br /> 0 nota(s) de 10,00 <br /> 1 nota(s) de 5,00 <br /> 1 nota(s) de 2,00 <br /> 0 nota(s) de 1,00 |
| *Exemplo 3* | 503 | 5 nota(s) de 100,00 <br /> 0 nota(s) de 50,00 <br /> 0 nota(s) de 20,00 <br /> 0 nota(s) de 10,00 <br /> 0 nota(s) de 5,00 <br /> 1 nota(s) de 2,00 <br /> 1 nota(s) de 1,00 |
"""



"""[1021](https://www.urionlinejudge.com.br/judge/pt/problems/view/1021) - Agora vamos voltar ao mundo real, onde trocos podem precisar utilizar cédulas e moedas.

Escreva um código Python que leia um valor de troco e informe quantas cédulas e moedas de cada valor devem ser entregues pelo vendedor ao cliente.

**Obs.:** Considere que ainda existem moedas de R$ 0,01.

|.| Entrada | Saída |
|-|----|---|
| *Exemplo 1* | 576.73 | NOTAS: <br /> 5 nota(s) de 100,00 <br /> 1 nota(s) de 50,00 <br /> 1 nota(s) de 20,00 <br /> 0 nota(s) de 10,00 <br /> 1 nota(s) de 5,00  <br /> 0 nota(s) de 2,00  <br /> MOEDAS: <br /> 1 moeda(s) de 1,00 <br /> 1 moeda(s) de 0,50 <br /> 0 moeda(s) de 0,25 <br /> 2 moeda(s) de 0,10 <br /> 0 moeda(s) de 0,05 <br /> 3 moeda(s) de 0,01 |
| *Exemplo 2* | 4.00 | NOTAS: <br /> 0 nota(s) de 100,00 <br /> 0 nota(s) de 50,00 <br /> 0 nota(s) de 20,00 <br /> 0 nota(s) de 10,00 <br /> 0 nota(s) de 5,00  <br /> 2 nota(s) de 2,00 <br /> MOEDAS: <br /> 0 moeda(s) de 1,00 <br /> 0 moeda(s) de 0,50 <br /> 0 moeda(s) de 0,25 <br /> 0 moeda(s) de 0,10 <br /> 0 moeda(s) de 0,05 <br /> 0 moeda(s) de 0,01 |
| *Exemplo 3* | 91.01 | NOTAS: <br /> 0 nota(s) de 100,00 <br /> 1 nota(s) de 50,00 <br /> 2 nota(s) de 20,00 <br /> 0 nota(s) de 10,00 <br /> 0 nota(s) de 5,00  <br /> 0 nota(s) de 2,00 <br /> MOEDAS: <br /> 1 moeda(s) de 1,00 <br /> 0 moeda(s) de 0,50 <br /> 0 moeda(s) de 0,25 <br /> 0 moeda(s) de 0,10 <br /> 0 moeda(s) de 0,05 <br /> 1 moeda(s) de 0,01 |
"""



"""[1019](https://www.urionlinejudge.com.br/judge/pt/problems/view/1019) - Sistemas de frente de loja também precisam registrar a data e o horário das vendas. 

Computadores normalmente armazenam datas utilizando uma única unidade de tempo, convertendo para o formato de apresentação desejado quando necessário. Por simplicidade, considere neste exercício que o dado informado representa apenas o horário da venda.

Escreva um código Python que leia um valor em segundos e o converta para o formato *horas:minutos:segundos*.

**Dica 1 --** a opção sep do procedimento print() permite configurar o caracter de separação entre as diferentes partes de uma impressão, como no exemplo abaixo.
"""

print(10,33,51,sep=":")

"""**Dica 2 --** é possível utilizar o procedimento print para impressão formatada. Pesquise o funcionamento da máscara de formatação abaixo:"""

print("%02d:%02d:%02d" % (9,33,51))

"""|.| Entrada | Saída |
|-|----|---|
| *Exemplo 1* | 556  | 00:09:16 | 
| *Exemplo 2* | 1 | 00:00:01 |
| *Exemplo 3* | 86153 | 23:55:53 |
"""
