from math_object import Math
from knew_time import  Time
from step import Step

math = Math()
time = Time()
step = Step('Math')

while True:
    funct = input(f'В зависимости оттого что вы хотите узнать введите цифру\n'\
                  f'1: узнать окончание уроков\n'\
                  f'2: узнать ср-ар оценку по математике\n'\
                  f'3: узнать сколько шагов осталось до кабинета {step.object}\n'\
                  f'если хотите выйти введите "q"    ')
    if funct == 'q' or funct == 'й':
        print('Программа завершена')
        break
    elif funct == '1':
        number_of_objects = int(input('Введите кол-во уроков на сегодня(от 2 до 9)          '))
        print(time.knew_time(number_of_objects))
    elif funct == '2':
        math.grade_book = (input('Введите ваши оценки через пробел              ')).split()
        print(math.get_average())
        math.grade_book = []
        math.sum_of_grades = 0

    elif funct == '3':
        print(step.step(20))

# math = Math()
#
# math.add(5)
# math.add(3)
# math.add(5)
# print(math.grade_book)
#
# print(math.get_average())




