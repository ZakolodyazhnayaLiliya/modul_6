# Домашнее задание по теме "Множественное наследование"
# Цель: закрепить знания множественного наследования в Python.
# Задача "Ошибка эволюции":
# Замечали, что некоторые животные в нашем мире обладают странными и, порой, несовместимыми друг с другом свойствами? Например, утконос... Вроде есть клюв, но не птица. Вроде милый, а есть шипы на задних лапах. А ещё он откладывает яйца... Опустим факт о том, что они потеют молоком и попробуем не эволюционным способом создать нашего утконоса.
# Необходимо написать 5 классов:
# Animal - класс описывающий животных.
import random
class Animal:
    # Класс обладает следующими атрибутами:
    live = True  # live = True
    sound = None  # sound = None - звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0  # _DEGREE_OF_DANGER = 0 - степень опасности существа
    def __init__(self, speed):
        # Объект этого класса обладает следующими атрибутами:
        self._cords = [0, 0, 0]  # _cords = [0, 0, 0] - координаты в пространстве.
        self.speed = speed  # speed = ... - скорость передвижения существа (определяется при создании объекта)
    # И методами:
    def move(self, dx, dy, dz):
        # move(self, dx, dy, dz), который должен менять соответствующие кооординаты в _cords на
        # dx, dy и dz в том же порядке, где множетелем будет являтся speed.
        # Если при попытке изменения координаты z в _cords значение будет меньше 0,
        # то выводить сообщение "It's too deep, i can't dive :(" , при этом изменения не вносяться.
        if self._cords[2] + dz >= 0:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed
        else:
            print("It's too deep, i can't dive :(")

    # get_cords(self), который выводит координаты в формате: "X: <координаты по x>,
    # Y: <координаты по y>, Z: <координаты по z>"
    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    # attack(self), который выводит "Sorry, i'm peaceful :)",
    # если степень опасности меньше 5 и "Be careful, i'm attacking you 0_0" , если равно или больше.
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    # speak(self), который выводит строку со звуком sound.
    def speak(self):
        if self.sound is not None:
            print(self.sound)
        else:
            print("I don't have any sound yet.")

# Bird - класс описывающий птиц. Наследуется от Animal.
# Должен обладать атрибутом:
# beak = True - наличие клюва

class Bird(Animal):
# задает атрибут класса - клюв
    beak = True
# И методом:
# lay_eggs(self), который выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you"
    def lay_eggs(self):
        num_eggs = random.randint(1, 4)
        print(f"Here are {num_eggs} eggs for you")

class AquaticAnimal(Animal):
    # В этом классе атрибут _DEGREE_OF_DANGER = 3.
    _DEGREE_OF_DANGER = 3# AquaticAnimal - класс описывающий плавающего животного. Наследуется от Animal.
    # Должен обладать методом:
    # dive_in(self, dz) - где dz изменение координаты z в _cords.
    # Этот метод должен всегда уменьшать координату z в _coords.
    # Чтобы сделать dz положительным, берите его значение по модулю (функция abs).
    # Скорость движения при нырянии должна уменьшаться в 2 раза, в отличии от обычного движения.
    # (speed / 2)
    def dive_in(self, dz):
        # создали новую переменную для расчета z
        new_cords =self._cords[2] - abs(dz) * .5 * self.speed
        self._cords[2] = max(new_cords, 0)

# PoisonousAnimal - класс описывающий ядовитых животных. Наследуется от Animal.

class PoisonousAnimal(Animal): # AquaticAnimal - класс описывающий плавающего животного. Наследуется от Animal.
    _DEGREE_OF_DANGER = 8

# Duckbill - класс описывающий утконоса. Наследуется от классов Bird, AquaticAnimal, PoisonousAnimal. Порядок наследования определите сами, опираясь на ниже приведённые примеры выполнения кода.
# Объект этого класса должен обладать одним дополнительным атрибутом:
# sound = "Click-click-click" - звук, который издаёт утконос
class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)



# print(Duckbill.mro())
# Пример работы программы:
db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()

