class Recipe:
    # Атрибут класу
    base_cost = 50  # Базова вартість (в умовних одиницях)

    def __init__(self, title="Невідомий рецепт", preparation_time=30, description="Опис відсутній"):
        self.title = title  # Назва рецепту (публічний)
        self._preparation_time = preparation_time  # Час приготування (захищений)
        self.__description = description  # Опис рецепту (приватний)

    # Властивості
    @property
    def preparation_time(self):
        return self._preparation_time

    @preparation_time.setter
    def preparation_time(self, value):
        if value > 0:
            self._preparation_time = value
        else:
            raise ValueError("Час приготування повинен бути більшим за 0 хвилин!")

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if value:
            self.__description = value
        else:
            raise ValueError("Опис не може бути порожнім!")

    # Метод для обчислення вартості рецепта
    def calculate_cost(self):
        return self._preparation_time * Recipe.base_cost

    # Статичний метод
    @staticmethod
    def validate_title(title):
        if len(title) < 3:
            return False
        return True

    # Перевизначення методу __str__
    def __str__(self):
        return f"Рецепт: {self.title}, Час приготування: {self._preparation_time} хв, Опис: {self.__description}"


class Ingredient:
    # Атрибут класу
    unit_cost = 5  # Базова вартість за одиницю інгредієнта

    def __init__(self, name="Невідомий інгредієнт", quantity=1, unit="шт"):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    # Властивості
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value > 0:
            self._quantity = value
        else:
            raise ValueError("Кількість повинна бути більшою за 0!")

    # Метод для розрахунку вартості інгредієнта
    def calculate_cost(self):
        return self._quantity * Ingredient.unit_cost

    # Декоратор методу
    def details_decorator(func):
        def wrapper(self):
            result = func(self)
            return f"[Деталі інгредієнта] {result}"
        return wrapper

    @details_decorator
    def details(self):
        return f"Інгредієнт: {self.name}, Кількість: {self.quantity} {self.unit}"

    # Перевизначення методу __str__
    def __str__(self):
        return f"Інгредієнт: {self.name}, Кількість: {self.quantity} {self.unit}"


# Демонстрація роботи класів
if __name__ == "__main__":
    # Створення рецепта
    recipe = Recipe("Борщ", 90, "Традиційна страва з України")
    print(recipe)

    # Оновлення опису
    recipe.description = "Нова версія борщу з унікальним смаком"
    print(f"Оновлений опис: {recipe.description}")

    # Додавання інгредієнта
    beetroot = Ingredient("Буряк", 2, "шт")
    print(beetroot)
    print(beetroot.details())

    # Розрахунок вартості рецепта
    print(f"Вартість рецепта '{recipe.title}': {recipe.calculate_cost()} одиниць")

    # Валідація назви
    print(f"Чи правильна назва рецепта? {Recipe.validate_title(recipe.title)}")

    # Розрахунок вартості інгредієнта
    print(f"Вартість інгредієнта '{beetroot.name}': {beetroot.calculate_cost()} одиниць")
