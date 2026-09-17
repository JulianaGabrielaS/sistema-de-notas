print('='*10,' SISTEMA DE NOTAS ', '='*10)

contador = 1
soma = 0

while True:
    nome_aluno = input('Nome do Aluno: ').strip().upper()
    if len(nome_aluno) >=3 and nome_aluno.replace(' ', '').isalpha():
        break
    else:
        print('Nome inválido. Digite apenas letras.')

while contador <= 3:
    nota = float(input(f'Digite sua {contador}º nota: '))

    if 0 <= nota <= 10:
        soma += nota #Acrescenta a nota na soma
        contador += 1
    else:
        print('Nota inválida. Digite uma nota entre 0 e 10.') 

print()
#Menu de escolha de tipo de ensino
print('='*10, 'TIPO DE ENSINO', '='*10)
print('[1] Ensino Fundamental')
print('[2] Ensino Médio')
print('[3] Ensino Integral\n')

#Validação da escolha
while True:
    escolha_ensino = int(input('Digite a opção: '))
    # Total de aulas definido conforme a carga horária anual de cada modalidade.
    if escolha_ensino == 1:
        total_aula = 1200
        break
    elif escolha_ensino == 2:
        total_aula = 1100
        break
    elif escolha_ensino == 3:
        total_aula = 1500
        break
    else:
        print('Opção inválida. Digite novamente.')

# Frequência
aulas_frequentadas = int(input(f'{nome_aluno}, quantas aulas você frequentou? '))

frequencia = aulas_frequentadas / total_aula * 100

media = soma / 3

print()
print('='*10, 'RESULTADO ', '='*10)
print(f'Aluno: {nome_aluno}')
print(f'Média: {media:.1f}')
print(f'Frequência: {frequencia:.1f}%')

if media >= 6 and frequencia >= 75:
    print('Situação: Aprovado.')
elif media >= 6 and frequencia < 75:
    print('Situação: Reprovado por frequência.')
elif media >= 5 and frequencia >= 75:
    print('Situação: Recuperação.')
elif media >= 5 and frequencia < 75:
    print('Situação: Recuperação por nota e frequência.')
elif media < 5 and frequencia >= 75:
    print('Situação: Reprovado por nota.')
else:
    print('Situação: Reprovado por nota e frequência.')

