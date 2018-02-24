grades = [('Ann', '9' ), ('John', '7' ), ('Smith', '5' ), ('George', '6' ) ]
i = 0
while i < len(grades):
    position = 0
    min = int(grades[position][1])
    for q in range(len(grades)):
        if int(grades[q][1]) < min:
            min = int(grades[q][1])
            position = q
    print('Hello {0}! Your grade is {1}'.format(grades[position][0],grades[position][1]))
    grades.pop(position)