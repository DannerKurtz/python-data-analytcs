age = '23' ## definindo uma variável do tipo string
age_integer = int(age) ## fazendoa a conversão para o tipo inteiro

print(type(age))
print(type(age_integer))

price = 9.99 ## definindo uma variável do tipo float
price_integer = int(price) ## fazendo a conversão para o tipo inteiro
price_string = str(price) ## fazendo a conversão para o tipo string
price_boolean = bool(price) ## fazendo a conversão para o tipo booleano
print (f'tipo do preço: {type(price)}, tipo do preço inteiro: {type(price_integer)}, tipo do preço string: {type(price_string)}, tipo de preço booleano: {type(price_boolean)}''')