#Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. Администраторы, помимо обычных данных пользователей,
# имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.
# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).
# 2.Класс `Admin`: Этот класс должен наследоваться от класса `User`. Добавь дополнительный атрибут уровня доступа,
# специфичный для администраторов ('admin'). Класс должен также содержать методы `add_user` и `remove_user`, которые позволяют добавлять и удалять
# пользователей из списка (представь, что это просто список экземпляров `User`).
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User():
    def __init__(self, user_id, user_name):
        self._user_id = user_id
        self._user_name = user_name
        self._access_level = "user"

    def get_user_id(self):
        return self._user_id

    def get_user_name(self):
        return self._user_name

    def get_level(self):
        return self._access_level

    def set_user_name (self, name):
        self._user_name = name


class Admin(User):
    def __init__(self, user_id, user_name):
        super().__init__(user_id, user_name)
        self._access_level = "admin"
        self.users = []


    def add_user(self, user):
        self.users.append(user)
        print(f"Пользователь {user.get_user_name()} добавлен.")

    def remove_user(self, user_name):
        found = False
        for user in self.users:
            if user.get_user_name() == user_name:
                self.users.remove(user)
                print(f"Пользователь {user.get_user_name()} удален.")
                found = True
                break
        if not found:
            print("Ошибка: Пользователь не найден.")

    def show_users(self):
        for user in self.users:
            print (f"ID: {user.get_user_id()}, Имя: {user.get_user_name()}")


admin1 = Admin("AD_23", "Петров АА")
user1 = User("34.40", "Иванов СВ")
user2 = User("35.70", "Сидоров ВА")

admin1.add_user(user1)
admin1.add_user(user2)

admin1.show_users()

admin1.remove_user(user2.get_user_name())

admin1.show_users()





