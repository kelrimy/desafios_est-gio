entrada = input("Digite uma string: ")
invertida = entrada[::-1]

print(f"String invertida: {invertida}")


# Alternativa sem uso de funções prontas
def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

entrada = input("Digite uma string: ")
print(f"String invertida: {inverter_string(entrada)}")



entrada = input("Digite uma string: ")
lista_chars = list(entrada)

lista_chars.reverse()

invertida = ''.join(lista_chars)
print(f"String invertida: {invertida}")
