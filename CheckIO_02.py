import re


text = input('Введите строку:  ')
if 0 < len(text) <= 10**5:
    print('Ok')
    print(text)
    text = text.lower()
    print(text)
    text_list = []
    fr_list = []
    fr_list_letter = []
    max_fr = 0
    for i in text:
        if re.match("[a-z]+", text):
            text_list.append(i)
    print(text_list)
    for el in text_list:
        fr = text_list.count(el)
        print(el, fr)
        if fr>max_fr:
            max_fr=fr
            fr_list_letter.append(el)
            fr_list.append(max_fr)
print(fr_list, len(fr_list))
print(fr_list_letter, len(fr_list_letter))
ggg = max(fr_list)
print(ggg)
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