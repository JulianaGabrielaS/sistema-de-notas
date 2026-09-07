print('=== SISTEMA DE NOTAS ===')

nome_aluno = input('Nome do Aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

if 0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10:
    media = (nota1 + nota2 + nota3) / 3

    print('=== RESULTADO ===')
    print('Aluno: ', nome_aluno)
    print('Média: ', media)

    if media >= 6:
        print('Situação: Aprovado.')
    elif media >= 5:
        print('Situação: Recuperação.')
    else:
        print('Situação: Reprovado.')
else:
    print('Nota inválida.')