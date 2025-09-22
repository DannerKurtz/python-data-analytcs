nome = input('Digite seu nome: ') ## Declara a variável nome e pede para o usuário digitar o nome
print('Olá,', nome) ## Imprime na tela a mensagem 'Olá,' e o conteúdo da variável nome
idade = input('Digite sua idade: ') ## Declara a variável idade e pede para o usuário digitar a idade
print(nome, idade) ## Imprime na tela o conteúdo da variável nome e o conteúdo da variável idade
print(nome, idade, end="...\n") ## Imprime na tela o conteúdo da variável nome e o conteúdo da variável idade, mas ao invés de pular uma linha, imprime "..."
print(nome, idade, sep="-") ## Imprime na tela o conteúdo da variável nome e o conteúdo da variável idade, mas ao invés de um espaço entre eles, imprime um hífen