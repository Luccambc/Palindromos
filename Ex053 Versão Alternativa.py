frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
frase_junta = ''.join(palavras)
inverso = frase_junta[::-1]                                                                                             # Fatiamento de strings

print(f"O inverso de {frase_junta} é {inverso}")
if inverso == frase_junta:
    print("Temos um palíndromo :)")
else:
    print("Não temos um palíndromo :(")

