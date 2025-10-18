"""
Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка і візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів. Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.



Вимоги до завдання:

Створіть віртуальне оточення Python для ізоляції залежностей проекту.
Скрипт має отримувати шлях до директорії як аргумент при запуску. Цей шлях вказує, де знаходиться директорія, структуру якої потрібно відобразити.
Використання бібліотеки colorama для реалізації кольорового виведення.
Скрипт має коректно відображати як імена директорій, так і імена файлів, використовуючи рекурсивний спосіб обходу директорій (можна, за бажанням, використати не рекурсивний спосіб).
Повинна бути перевірка та обробка помилок, наприклад, якщо вказаний шлях не існує або він не веде до директорії.
"""

import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama
init(autoreset=True)


def print_dir_structure(path: Path, prefix=""):
    """
    Рекурсивно виводить структуру директорій з кольорами.
    Директорії — голубим, файли — зеленим.
    """
    if not path.exists():
        print(Fore.RED + f"Шлях {path} не існує!")
        return
    if not path.is_dir():
        print(Fore.RED + f"Шлях {path} не є директорією!")
        return

    for item in sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower())):
        if item.is_dir():
            print(f"{prefix}{Fore.CYAN}📂 {item.name}{Style.RESET_ALL}")
            print_dir_structure(item, prefix + " ┃ ")
        else:
            print(f"{prefix}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")


def main():
    """Основна функція програми."""
    if len(sys.argv) < 2:
        print(Fore.RED + "Помилка: потрібно вказати шлях до директорії при запуску скрипта!")
        sys.exit(1)

    arg_path = sys.argv[1]
    dir_path = Path(arg_path).resolve()

    print(Fore.MAGENTA + f"📦 {dir_path.name}" + Style.RESET_ALL)
    print_dir_structure(dir_path)


if __name__ == "__main__":
    main()


