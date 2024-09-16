notas = [6.3, 7.5, 9.2, 5.1, 6.8]

soma_notas = sum(notas)
quantidade_notas = len(notas)
media = soma_notas / quantidade_notas

notas_acima_da_media = sum(nota > 6 for nota in notas)

print("A média das notas é: ", media)
print("A quantidade de notas acima da média (6) é:", notas_acima_da_media)