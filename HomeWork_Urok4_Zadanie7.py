line = input('Enter line: ')
symbol = input('Enter symbol:')
print('Original line ', line)
counter = 0
L = []
for i in range(len(line)):
    if line[i] == symbol:
        L.append(i)
        counter +=1
for i in range(len(L)):
    if i+1 == len(L):
        line1 = line[:L[i]]
        line = line1
    else:
        line1 = line[:L[i]] + line[L[i]].upper() + line[L[i]+1:len(line)]
        line = line1

print('Converted line',line)