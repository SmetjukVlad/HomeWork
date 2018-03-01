def inp():
    line = input('Enter line: ')
    return line

def search(x):
    dict = {}
    for i in x:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print('Max value is {}, num: {}'.format(*max(dict.items(), key = lambda x: x[1])))

line = inp()
search(line)