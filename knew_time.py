import math

class Time:
    def knew_time(self, number_of_objects):
        if 1 < number_of_objects < 10:
            time = 8.00
            if number_of_objects < 4:
                time += (number_of_objects * (45 + 5) - 5) / 60
            else:
                pause = (number_of_objects - 4) // 3 + 1
                time += ((number_of_objects * (45 + 5) - 5) + pause * 15 - pause * 5) / 60
            return f'конец урока в {int(time)} : {math.ceil((time % 1) * 60)}\n'

        else:
            return f'Неправильное кол-во уроков\n'