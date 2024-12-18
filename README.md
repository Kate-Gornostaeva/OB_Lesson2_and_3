# OB_Lesson2_and_3
 task for OB_Lesson2 and 3
 # Zoo Management System

Это простая система управления зоопарком, написанная на Python. Она позволяет моделировать животных, их звуки и диету, а также управление зоопарком и его сотрудниками.

## Описание

Система состоит из следующих компонентов:

- **Животные**: Базовый класс `Animal` и его подклассы для различных типов животных (птицы, млекопитающие, рептилии).
- **Зоопарк**: Класс `Zoo`, который содержит список животных и сотрудников.
- **Сотрудники**: Классы `Zookeeper` и `Vet` для управления животными (кормление и лечение).

## Структура классов

1. **Animal**
   - Атрибуты: `name`, `color`
   - Методы: `make_sound()`, `eat()`

2. **Bird** (наследуется от Animal)
   - Звук: "Чирик-чирик"
   - Питание: "Зерно, насекомые"

3. **MammalHerbivore** (наследуется от Animal)
   - Звук: "Муу"
   - Питание: "Трава, зерно, сено"

4. **MammalPredator** (наследуется от Animal)
   - Звук: "Грр-рр-р"
   - Питание: "Мясо"

5. **Reptile** (наследуется от Animal)
   - Звук: "Хссс-ссс"
   - Питание: "Насекомые, мелкие млекопитающие"

6. **Zoo**
   - Атрибуты: `animals`, `workers`
   - Методы: `add_new_animal()`, `add_new_worker()`

7. **Zookeeper**
   - Атрибут: `name`
   - Метод: `feed_animal()`

8. **Vet**
   - Атрибут: `name`
   - Метод: `heal_animal()`

