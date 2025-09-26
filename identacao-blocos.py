limit = 100

def sacar(amount):
  if amount >= limit: 
    print('valor indisponivel')
  else:
    print('valor disponivel')
  print('obrigado pelo saque!')

sacar(amount=200)

