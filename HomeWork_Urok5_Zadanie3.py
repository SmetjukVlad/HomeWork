dbase = [{'name': 'Vlad','surname': 'Smetjuk', 'gender':'male', 'age': '28'},
         {'name':'Ivan','surname':'Petrov','gender': 'male', 'age':'20'},
         {'name':'Katja','surname':'Ivanova','gender':'female', 'age':'28'}]

condition = (input('Введите условия поиска. Например name=Vlad&age=28:')).split('&')

cond = []

for i in range(len(condition)):     # разделение условия на ключи
    sep = condition[i].split('=')
    cond.append({sep[0]:sep[1]})

len_base = len(dbase)
len_cond = len(cond)
counter1 = 0
for i in range(len(dbase)):
    counter = 0
    line1_key = list(dbase[i].keys())
    line1_values = list(dbase[i].values())

    for w in range(len(line1_key)):
        for q in range(len(cond)):
            line2_key = list(cond[q].keys())
            line2_values = list(cond[q].values())
            if line1_key[w] == line2_key[0] and line1_values[w] == line2_values[0]:
                counter += 1


    if counter == len_cond:
        counter1 +=1
        print('Подходящая по поиску запись: {} Имя {} Фамилия {}  Пол {} Возраст {}'.format(counter1,
            dbase[i]['name'],dbase[i]['surname'],dbase[i]['gender'],dbase[i]['age']))


