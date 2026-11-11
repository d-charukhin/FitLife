# Проект FitLife - MVP версия 1.0


# 1. Знакомство
user_name = input("Введи ваше имя: ")
user_age = int(input("Введите ваш возраст: "))


# 2. Сбор данных
user_weight = float(input("Введите ваш вес(кг): "))
user_height = float(input("Введите ваш рост(м), например 1.78: "))


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = round(user_weight / (user_height ** 2), 1)


# Подсчет воды: вес * 30 мл
water_ml = user_weight * 30
water_needed = round(water_ml / 1000, 2)


# 4. Вывод красивого результата
print(f"Привет!, {user_name.title()}")
print(f"Твой возраст: {user_age} г. ИМТ: {bmi}, норма воды: {water_needed}")
print("Расчет окончен. Будьте здоровы!")
