turma = ('André', 'Fernanda', 'Luiz')

nome_aluno = input("Digite o nome do aluno: ")

if nome_aluno in turma:
    print(f"{nome_aluno} está presente na turma.")
else:
    print(f"{nome_aluno} não está presente na turma.")