frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()                                                                                                # Separando a string em palavaras separadas (Formando um vetor)
frase_junta = ''.join(palavras)                                                                                         # Juntando as palavras e eliminando os espaços entre elas
inverso = ''

for letra in range(len(frase_junta) - 1, -1, -1):
    inverso += frase_junta[letra]
print(f"O inverso de {frase_junta} é {inverso}")
if inverso == frase_junta:
    print("Temos um palíndromo :)")
else:
    print("Não temos um palíndromo :(")

