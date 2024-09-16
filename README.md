# Desafios de Programação para Estágio

Este repositório contém soluções para uma série de desafios de programação apresentados como parte do processo seletivo para estágio. Cada desafio aborda uma habilidade específica de programação e resolução de problemas.

## Índice

1. [Cálculo da Soma](#cálculo-da-soma)  
2. [Sequência de Fibonacci](#sequência-de-fibonacci)  
3. [Faturamento Diário](#faturamento-diário)  
4. [Percentual de Representação por Estado](#percentual-de-representação-por-estado)  
5. [Inversão de String](#inversão-de-string)
6. [Contato](#contato)


### Cálculo da Soma

**Descrição:**  
1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;  
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }  
Imprimir(SOMA);  
Ao final do processamento, qual será o valor da variável SOMA?  

```python
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)
#Resultado: 91

```

**Explicação:** Este desafio envolve compreender o funcionamento de um loop que incrementa uma variável `K` e acumula seu valor na variável `SOMA`. O código incrementa `K` até que ele atinja um valor predefinido (`INDICE`), somando `K` a `SOMA` em cada iteração.

### Sequência de Fibonacci

**Descrição:**  
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

```python

def fibonacci(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

numero = int(input("Digite um número: "))

if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")


```

**Explicação:** O desafio exige a implementação de um algoritmo para gerar a sequência de Fibonacci e verificar se um número específico está presente nela. O número pode ser fornecido pelo usuário ou definido no código.

### Faturamento Diário

**Descrição:**  
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:  
• O menor valor de faturamento ocorrido em um dia do mês;  
• O maior valor de faturamento ocorrido em um dia do mês;  
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.  
IMPORTANTE:  
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;  
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;  

```python
import json

faturamento_json = '''
{
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}
'''

faturamento = json.loads(faturamento_json)

valores = list(faturamento.values())
menor = min(valores)
maior = max(valores)
media = sum(valores) / len(valores)
dias_acima_media = len([v for v in valores if v > media])

print(f"Menor valor de faturamento: R${menor:.2f}")
print(f"Maior valor de faturamento: R${maior:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

```

**Explicação:** Este desafio envolve a manipulação de dados em JSON ou XML para calcular estatísticas sobre o faturamento diário. O programa deve calcular a média mensal e identificar os dias com faturamento acima dessa média.

### Percentual de Representação por Estado

**Descrição:**  
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:  
• SP – R$67.836,43  
• RJ – R$36.678,66  
• MG – R$29.229,88  
• ES – R$27.165,48  
• Outros – R$19.849,53  

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

```python
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento.values())
percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

```

**Explicação:** O desafio envolve realizar cálculos percentuais para determinar a contribuição de cada estado para o faturamento total. É um exercício de manipulação e análise de dados financeiros.

### Inversão de String

**Descrição:**  
5) Escreva um programa que inverta os caracteres de um string.  
IMPORTANTE:  
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;  
b) Evite usar funções prontas, como, por exemplo, reverse;  

**Opções de Resolução:**  
```python
entrada = input("Digite uma string: ")
invertida = entrada[::-1]

print(f"String invertida: {invertida}")
```  

```python
# Alternativa sem uso de funções prontas
def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

entrada = input("Digite uma string: ")
print(f"String invertida: {inverter_string(entrada)}")
```  



**Explicação:** Este desafio exige a implementação de um algoritmo para inverter uma string sem usar funções prontas que realizam essa tarefa. O objetivo é praticar a manipulação de strings e as habilidades básicas de programação.

## Instruções de Uso

Para rodar os programas, clone o repositório e execute os arquivos na linguagem desejada. Certifique-se de ter o ambiente de desenvolvimento adequado para a linguagem utilizada.

## Contato

   Email: kelrimymbb@gmail.com  
   Linkedin: https://www.linkedin.com/in/kelrimy/
