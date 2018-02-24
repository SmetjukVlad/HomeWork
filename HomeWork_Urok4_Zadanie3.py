L=[]
while True:
    line = input('Enter line ')
    if line != '':
        L.append(line)
    else:
        break
print(L)
lenght = len(L[0])
position = 0
L1=[]
q = 1
for i in range(len(L)):
    if len(L[i]) > lenght:
        lenght = len(L[i])
        position = i
        L1 = []
        L1.append(i+1)
    elif len(L[i]) == lenght:
        L1.append(i+1)

if len(L1) == 1:
    print('Longest line is {0}. Lenght is {1}'.format(position+1,lenght))
else:
    print('Quantity of longest lines is {}'.format(len(L1)))
    print('Position of lines', end = ' '),
    for i in range(len(L1)):
        print(' ', L1[i], end = ' ')