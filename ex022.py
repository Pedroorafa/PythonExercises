#nome com todas as letras maiusculas V
#nome com todas as letras minusculas
#quantas letras ao todo, sem espacos
#quantas letras tem o primeiro nome
nome = str(input('Digite algo ').strip())
nome2 = nome.split()
nome3 =''.join(nome2)
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome tem {} letras ao todo'.format(nome3.__len__()))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome2[0], nome2[0].__len__()))

