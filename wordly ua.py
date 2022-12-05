#wordly by zrv
from random import choice
word = ('слово','заєць',
        'ворон','школа','кулон','місто','стіна')
select = choice(word)
print (select)
print (f'Вгадай слово.\nВоно має {len(select)} букв')
#----------------------------------------
def star(myInput, select):
    answer = []
    answer2 = []
    for i in range (len(select)):
        if myInput[i] == select[i]:
           answer.append(select[i])
        else:
            answer.append('*')
    for i in range (len(select)):
        if select.find(myInput[i]) > -1:
            answer2.append(myInput[i])
    return f'{answer}\n{answer2}'

#---------------------------------------
def what(a,b):
    if a.find(b) != -1:
        print ('Ви вгадали загадане слово')
        return False
    else:
        print('---------------\nСпробуй ще\n--------------')
        if len(a) != len(b):
            print('Невірна довжина слова')
        else:
            wordStar = star(a,b)
            print(f'{wordStar}')
        return True

#--------------------------------------------
while True:
    if what(input(),select) != True:
        break