import random

# Генерация случайных данных
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

# Создание словаря с уникальными значениями
unique_values = set(lst)

# Преобразование данных в one hot формат
one_hot_encoded = []
for value in lst:
    encoded_value = [1 if value == unique_value else 0 for unique_value in unique_values]
    one_hot_encoded.append(encoded_value)

# Отображение результатов
for i in range(len(one_hot_encoded)):
    print(one_hot_encoded[i])
