line = input('Enter the list with a space: ')
L = line.split(' ')
while True:
    q = 1
    for i in range(len(L)):
        if L[i] == '0':
            L.remove('0')
            L.append('-1')
            q = 0
    if q == 0:
        continue
    else:
        break
print('Converted list is: {}'.format(L))