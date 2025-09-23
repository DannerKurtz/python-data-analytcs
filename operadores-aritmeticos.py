product_01 = 10
product_02 = 20

print(f'soma dos produtos 01 e 02: {product_01 + product_02}')  # soma
print(f'subtração dos produtos 01 e 02: {product_01 - product_02}')  # subtração
print(f'multiplicação dos produtos 01 e 02: {product_01 * product_02}')  # multiplicação
print(f'divisão dos produtos 01 e 02: {product_01 / product_02}')  # divisão
print(f'divisão inteira dos produtos 01 e 02: {product_01 // product_02}') # divisão inteira
print(f'resto da divisão dos produtos 01 e 02: {product_01 % product_02}')  # resto da divisão
print(f'potência dos produtos 01 e 02: {product_01 ** product_02}') # potência

# Ordem de precedência: (), **, *, /, //, %, +, -
print(f'Exemplo de ordem de precedência produto 01 + produto 02 * produto 01: {product_01 + product_02 * product_01}')  # sem parênteses
print(f'Exemplo de ordem de precedência (produto 01 + produto 02) * produto 01: {(product_01 + product_02) * product_01}')  # com parênteses