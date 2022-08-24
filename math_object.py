


class Math:
    def __init__(self):
        self.__grade_book = []
        self.__sum_of_grades = 0

    @property
    def grade_book(self):
        return self.__grade_book

    @grade_book.setter
    def grade_book(self, value):
        self.__grade_book = value

    @property
    def sum_of_grades(self):
        return self.__sum_of_grades

    @sum_of_grades.setter
    def sum_of_grades(self, value):
        self.__sum_of_grades = value

    def add(self, grade):
        self.__grade_book.append(grade)

    def get_average(self):
        for i in self.__grade_book:
            self.__sum_of_grades += int(i)

        return f'Средняя оценка по математике {round(self.__sum_of_grades / len(self.__grade_book), 2)}\n'


