c = 0
while True:
    n = int(input('Quer saber a tabuada de qual número? '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
        c += 1
print('FIM')
