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
