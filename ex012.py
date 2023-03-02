produto = float(input('Qual o preço do produto? '))
desconto  = produto/100*5
print('O produto de valor {} receberá um desconto de 5%'.format(produto), end=' ')
print('passando a custar {} reais'.format(produto-desconto))

