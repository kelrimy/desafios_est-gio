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

