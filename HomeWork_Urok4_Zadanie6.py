line = input('Enter the list with a space: ')
L = line.split(' ')
L1 = []
position = 0
q = 0
counter = 0
while q < len(L):

      #for i in range(len(L)):
    if counter == 0:

        if int(L[q]) < 0:
            L1 = []
            L1.append(L[q])
            L1 = L1 + L[:q]+L[q+1:len(L)]
            L = L1
            counter += 1

    else:
        if int(L[q]) < 0:
            i = 0
            L1 = []
            while i < counter:
                L1.append(L[i])
                i += 1

            L1.append(L[q])

            L1 = L1 + L[0+counter:q]+L[q+1:len(L)]
            L = L1
            counter += 1
    q += 1
print('Transformed array:',L)