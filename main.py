# Импортируем библиотеку PySimpleGUI для создания графического интерфейса
import PySimpleGUI as sg
# Импортируем библиотеку math для математических операций
import math
# Импортируем библиотеку datetime для работы с датой и временем
import datetime
# Импортируем библиотеку random для генерации случайных чисел
import random

# Функция для вычисления квадратного корня из числа
def calculate_square_root(number):
    return math.sqrt(number)

# Функция для получения текущей даты и времени
def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Функция для генерации случайного числа от 1 до 100
def generate_random_number():
    return random.randint(1, 100)

# Устанавливаем тему оформления для графического интерфейса PySimpleGUI
sg.theme("DarkBlue3")

# Создаем макет окна с использованием элементов PySimpleGUI
layout = [
    # Строка для ввода числа и кнопка для вычисления квадратного корня
    [sg.Text("1. Введите число:"), sg.InputText(key="number_input"), sg.Button("Вычислить квадратный корень")],
    # Строка для вывода текущей даты и времени
    [sg.Text("2. Текущая дата и время:"), sg.Text("", size=(30, 1), key="date_output")],
    # Кнопка для обновления даты и времени
    [sg.Button("Обновить дату и время")],
    # Строка для вывода случайного числа
    [sg.Text("3. Сгенерировать случайное число от 1 до 100:"), sg.Text("", size=(30, 1), key="random_number_output")],
    # Кнопка для генерации случайного числа
    [sg.Button("Сгенерировать число")],
    # Кнопка для выхода из программы
    [sg.Button("Выход")]
]

# Создаем окно с использованием макета
window = sg.Window("Демонстрация функций в Python", layout)

# Основной цикл обработки событий окна
while True:
    # Получаем событие и значения элементов окна
    event, values = window.read()

    # Проверяем событие на закрытие окна
    if event == sg.WIN_CLOSED or event == "Выход":
        break
    # Если нажата кнопка "Вычислить квадратный корень"
    elif event == "Вычислить квадратный корень":
        try:
            # Преобразуем введенное значение в число и вычисляем квадратный корень
            number_input = float(values["number_input"]) if values["number_input"].replace(".", "").isdigit() else 0
            result = calculate_square_root(number_input)
            # Выводим сообщение с результатом
            sg.popup(f"Квадратный корень из {number_input} равен {result:.2f}")
        except ValueError:
            # В случае ошибки выводим сообщение об ошибке
            sg.popup_error("Введите корректное число.")
    # Если нажата кнопка "Обновить дату и время"
    elif event == "Обновить дату и время":
        # Получаем текущую дату и время
        current_date = get_current_date()
        # Обновляем текстовую метку с текущей датой и временем
        window["date_output"].update(current_date)
    # Если нажата кнопка "Сгенерировать число"
    elif event == "Сгенерировать число":
        # Генерируем случайное число от 1 до 100
        random_number = generate_random_number()
        # Обновляем текстовую метку с сгенерированным числом
        window["random_number_output"].update(f"{random_number}")

# Закрываем окно после выхода из цикла
window.close()
