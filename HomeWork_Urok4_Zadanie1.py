import string as st1
num = input('Enter word: ')
signs = st1.punctuation
index = signs.find('_')
signs_new = signs[0:index] + signs[int(index+1):len(signs)]
counter = 0
for i in signs_new:
    if i == num[0]:
        counter += 1
if counter == 0:
    print('This word {} is identifier'.format(num))
else:
    print('This word {} is not identifier'.format(num))
