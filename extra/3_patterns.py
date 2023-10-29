"""
Паттерны проектирования. Хотя бы синглтон
"""
import random
from collections import defaultdict
from functools import lru_cache


ALL_DRINKS = defaultdict(int)


class Drink:
    """Интерфейс напитка."""

    def main(self):
        raise NotImplemented


class Water(Drink):
    """Вода."""

    def main(self) -> str:
        return 'вода'


class Juice(Drink):
    """Сок."""

    def main(self) -> str:
        return 'Сок'


# декоратор
def drink_counter(func):
    """Считает кол-во выданных напитков."""

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        ALL_DRINKS[result.__class__.__name__] += 1
        return result

    return wrapper


# фабрика
@drink_counter
def get_drink(price: int) -> Drink:
    """Выдаёт какой-то напиток в зависимости от цены."""
    if price <= 10:
        return Water()

    return Juice()


for _ in range(10):
    drink = get_drink(random.randint(1, 20))

print(ALL_DRINKS)


# Синглтон
unique_juice = Juice()


# либо так
@lru_cache
def get_unique_juice():
    return Juice()
