# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите
# методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и
# сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например, `feed_animal()` для
# `ZooKeeper` и `heal_animal()` для `Veterinarian`).

class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def make_sound(self):
        pass

    def eat(self, animals):
        for animal in zoo.animals:
            return

class Bird (Animal):
    def __init__(self, name, color):
        super().__init__(name, color)

    def make_sound(self):
        return "Чирик-чирик"

    def eat(self):
        return "Зерно, насекомые"

class MammalHerbivore (Animal):
    def __init__(self, name, color):
        super().__init__(name, color)

    def make_sound(self):
        return "Муу"

    def eat(self):
        return "Трава, зерно, сено"

class MammalPredator (Animal):

    def __init__(self, name, color):
        super().__init__(name, color)


    def make_sound(self):
        return "Грр-рр-р"

    def eat(self):
        return "Мясо"

class Reptile (Animal):

    def __init__(self, name, color):
        super().__init__(name, color)


    def make_sound(self):
        return "Хссс-ссс"

    def eat(self):
        return "Насекомые, мелкие млекопитающие"

def animal_sounds (animals):
    for animal in animals:
        print(f"\n{animal.name} ({animal.color}) издает звук: {animal.make_sound()}")


class Zoo:
    def __init__(self):
        self.animals=[]
        self.workers=[]


    def add_new_animal(self, animal):
        self.animals.append(animal)
        print(f"Новое животное {animal.name} в списке.")


    def add_new_worker(self, worker):
        self.workers.append(worker)
        print(f"Новый сотрудник {worker.name} в списке.")


class Zookeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        for animal in zoo.animals:
            print(f"Смотритель зоопарка {self.name} кормит животное:{animal.name}. Рацион животного: {animal.eat()}")


class Vet:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"Ветеринар {self.name} лечит животное: {animal.name}")


bird = Bird("грач", "черный")
cow = MammalHerbivore("корова", "рыжая")
tiger = MammalPredator("тигр", "полосатый")
snake = Reptile("змея", "зеленая")

zoo = Zoo()
zoo.add_new_animal(bird)
zoo.add_new_animal(cow)
zoo.add_new_animal(tiger)
zoo.add_new_animal(snake)

animal_sounds(zoo.animals)
print("")
zookeeper = Zookeeper("Иванов СВ")
vet = Vet("Сидоров НИ")

zoo.add_new_worker(zookeeper)
zoo.add_new_worker(vet)
print("")
zookeeper.feed_animal(tiger)

vet.heal_animal(cow)



