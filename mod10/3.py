# Добавим в класс Animal переменную класса color, значение которой изначально равно "white", 
# и метод change_color, который должен менять значение переменной класса color.
# Создайте экземпляры объекта: first_animal и second_animal
#Вызовите функцию change_color("red") для любого экземпляра объекта Animal и 
# измените значение переменной класса color на "red".


class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self,color):
        Animal.color = color

    
first_animal = Animal('king', 10)       
second_animal = Animal('snack', 20)
first_animal.change_color('red')
second_animal.change_color('red')

