""" Задана натуральная степень k. Сформировать случайным образом список коэффициентов
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:

k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 """

""" Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов. """  #firstfile.txt     secfile.txt     thirdfile.txt

import random

def write_file(name,st):   #Записываем в файл многочлены в name ()
    with open(name, 'w') as data:
        data.write(st)

 
def enter_randoms():   # создание рандома 0 - 100
    return random.randint(0,101)

def create_polynomial(k):
    lst = [enter_randoms() for i in range(k+1)]
    return lst
    

def create_str(str_polin):                             #Записываем многочлен в строку  ***(нарезка от 1-го до последнего с шагом 1 в обратном порядке   arr[::-1])***
    lst= str_polin[::-1]
    n = ''
    if len(lst) < 1:
        n = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                n += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    n += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                n += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    n += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                n += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                n += ' = 0'
    return n

#Сложение многочленов


##################################################################################################################################################

k1 = int(input('Введите число k для первого многочлена = '))
k2 = int(input('введите число k для второго многочлена = '))

polynomial_first = create_polynomial(k1) #Создаем многочлены для первого файла
polynomial_second = create_polynomial(k2) #    для второго файла

write_file('firstfile.txt', create_str(polynomial_first))                                            #Записывается только строка !перевести в стр
write_file('secfile.txt', create_str(polynomial_second))



with open('firstfile.txt', 'r') as data:   #Считываем и выводим записанные многочлены
    pol1 = data.readlines()
with open('secfile.txt', 'r') as data:
    pol2 = data.readlines()
    
print(f"Первый многочлен {pol1}")
print(f"Второй многочлен {pol2}")
##### не трогай, работает

### сложение  многочлена