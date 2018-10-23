import re

text = input('Введите строку:  ')
if 0 < len(text) <= 10 ** 5:
    print('Ok')
    print(text)
    text = text.lower()     # переводим все символы в нижний регистр
    print(text)
    text_list = []          # создаем пустой список для занесения в него букв
    fr_list = []            # создаем пустой список для занесения в него частоты повторений
    fr_list_letter = []     # создаем пустой список для занесения в него наиболее встречающихся букв
    max_fr = 0              # определяем переменную для максимального количества повторений
    for i in text:          # проверяе буква это или нет
        if i.isalpha():
            text_list.append(i)
    print(text_list)
    for el in text_list:    # считаем для каждой буквы количество повторений
        fr = text_list.count(el)
        print(el, fr)
        if fr > max_fr:     # проверяем счетчик количества повторений (и он заносит в список первое же повторение, независимо от                                того какое это значение)
            max_fr = fr
            fr_list_letter.append(el)
            fr_list.append(max_fr)
print(fr_list, len(fr_list))
print(fr_list_letter, len(fr_list_letter))
fr_list_letter.pop(0)       # удаляем это первое значение (хотя оно может быть и верным)
print(fr_list_letter, len(fr_list_letter))
fr_list_letter.sort()       # сортируем
res = fr_list_letter[0]     # и определяем результат
print(res)
# for num in fr_list:


#
# count = 0
# max_count = 0
#
# for b in text_list:
#     most_fr_letter
#
#
#
#
#
#     if b == r:
#         count += 1
#         if count > max_count:
#             max_count = count
#             most_fr_letter.insert(0,b)
#             print('наиболее',most_fr_letter)
#
# print(r, count)
# print(type(r), type(count))
