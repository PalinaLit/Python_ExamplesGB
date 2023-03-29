# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков. 

# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 

# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12


dict_ru = {
    1:  'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЁЬЯ',
    4:'ЙЫ',
    5:'ЖЗХЦЧ',
    8: 'ШЭЮ',
    10: 'ФЩЪ'
}



word = input().upper()

result = 0

for i in word:
    for j in dict_ru:
        if i.upper() in dict_ru[j]:
            result += j

print(result)


# sum: суммировать содержимое итерируемого.

# ??????!
# print(sum([k for i in word for k, j in dict_ru.items() if i in j]))
# list_1 = [exp for item in iterable (if conditional)]
  
# [expression1(item)                                        for item in iterable]

# [expression1(item) if conditional1                        for item in iterable]

# [expression1(item) if conditional1 else expression2(item) for item in iterable]

# [expression1(item) if conditional1 else expression2(item) for item in iterable if conditional2]




    








