A = [ 'A' , 'E' , 'I' , 'O' , 'U']
a = [ 'a' , 'e' , 'i' , 'o' , 'u']
str = input('Enter sentence: ')
my_str = str.split(' ')
q = 1
while q == 1:
    for i in range(len(my_str)):
        if my_str[i] =='':
            pos = i
            q = 1
            break
        else:
            q = 0
    if q == 1:
        del my_str[pos]
position = 0
quantity = len(my_str[0])

for i in range(len(my_str)):
    if len(my_str[i]) <= quantity:
        position = i
        quantity = len(my_str[i])
min = my_str[position]
counter = 0
# i = 0

for i in range(len(min)):
    for q in range(len(a)):
        if min[i] == a[q] or min[i] == A[q]:
            counter +=1

print('shortest word: ', my_str[position])
print('shortest word have {} vowels'.format(counter))

