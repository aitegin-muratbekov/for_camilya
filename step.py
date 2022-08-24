class Step:
    def __init__(self, object):
        self.__object = object

    @property
    def object(self):
        return self.__object

    def step(self, how_metres):
        return f'До кабинета {self.__object} всего {how_metres*2} шагов    \n'
