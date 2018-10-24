


text = input('String:')
text = text.lower()  # переводим все символы в нижний регистр

letter_list = []
freq_list = []
max_freq = 0
max_freq_list = []
count = 0
finish_list = []
# letter = []
# проверяем длину
if 0 < len(text) <= 10 ** 5:
    for symbol in text:
        if symbol.isalpha():
            letter_list += symbol
    # print(letter_list, len(letter_list))
# считаем для списка из букв количесво повторений
    for freqency in letter_list:
        freq_list.append(letter_list.count(freqency))
    print(freq_list, len(freq_list))
# определяем максимальное количество повторений
    for el in freq_list:
        max_freq = max(freq_list)
    print(max_freq)
# заносим в новый список значения с максимальным количеством повторений
    for freq_number in freq_list:
        if freq_number == max_freq:
            finish_list.append(letter_list[count])
        count += 1
    # print(finish_list)
    # сортируем список
    finish_list.sort()
    # определяем искомую букву
    letter = finish_list[0]
    print(letter)
    print(type(letter))