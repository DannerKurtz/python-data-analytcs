print(f'Verdadeiro e Verdadeiro: {True and True}')
print(f'Verdadeiro e Falso: {True and False}')
print(f'Falso e Verdadeiro: {False and True}')
print(f'Falso e Falso: {False and False}')  

print('---' * 10)

print(f'Verdadeiro ou Verdadeiro: {True or True}')
print(f'Verdadeiro ou Falso: {True or False}')
print(f'Falso ou Verdadeiro: {False or True}')
print(f'Falso ou Falso: {False or False}')

print('---' * 10)

print(f'Negação de Verdadeiro: {not True}')
print(f'Negação de Falso: {not False}')

print('---' * 10)

saldo = 1000
saque = 200
limite = 400
conta_especial = True

exp_1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp_1)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)  

exp_3 = saldo >= saque and (saque <= limite or conta_especial) and saldo >= saque
print(exp_3)  

