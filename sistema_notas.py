print('=== SISTEMA DE NOTAS ===')

contador = 1
soma = 0

nome_aluno = input('Nome do Aluno: ')

while contador <= 3:
    nota = float(input(f'Digite sua {contador}º nota: '))

    if 0 <= nota <= 10:
        soma += nota #Acrescenta a nota na soma
        contador += 1
    else:
        print('Nota inválida. Digite uma nota entre 0 e 10.') 

media = soma / 3

print('=== RESULTADO ===')
print(f'Aluno: {nome_aluno}')
print(f'Média: {media:.1f}')

if media >= 6:
    print('Situação: Aprovado.')
elif media >= 5:
    print('Situação: Recuperação.')
else:
    print('Situação: Reprovado.')

#próximas melhorias:
# - validar o nome do aluno
# - adicionar percentual de presença
# - considerar nota + frequência na situação final