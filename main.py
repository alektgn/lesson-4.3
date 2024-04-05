from abc import ABC, abstractmethod


# Шаг 1: Создание абстрактного класса для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


# Шаг 2: Реализация конкретных типов оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."


class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."


# Дополнительный тип оружия для демонстрации расширяемости
class MagicWand(Weapon):
    def attack(self):
        return "Боец применяет магический удар."


# Шаг 3: Модификация класса Fighter
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def changeWeapon(self, new_weapon: Weapon):
        self.weapon = new_weapon

    def perform_attack(self):
        print(self.weapon.attack())


# Шаг 4: Реализация боя
class Monster:
    pass


def battle(fighter, monster):
    # Простая демонстрация боя
    fighter.perform_attack()
    # Здесь может быть логика определения победителя
    print("Монстр побежден!")


# Демонстрация использования
fighter = Fighter(Sword())  # Боец с мечом
monster = Monster()

battle(fighter, monster)

fighter.changeWeapon(Bow())  # Боец меняет оружие на лук
battle(fighter, monster)

# Добавление и использование нового типа оружия, не меняя остальной код
fighter.changeWeapon(MagicWand())
battle(fighter, monster)