# 3. В некоторой школе решили набрать три новых математических класса 
# и оборудовать кабинеты для них новыми партами. 
# За каждой партой может сидеть два учащихся. 
# Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.

# **Input:**

# 20

# 21

# 22

# **Output:**

print(f"Введите количесвто учеников первого класса")
a = int(input())

print(f"Введите количесвто учеников второго класса")
b = int(input())

print(f"Введите количесвто учеников третьего класса")
c = int(input())

import math
aAnswer = math.ceil(a/2)
print(f"Необходимое количество парт для учеников первого класса – {aAnswer}")
bAnswer = math.ceil(b/2)
print(f"Необходимое количество парт для учеников второго класса – {bAnswer}")
cAnswer = math.ceil(c/2)
print(f"Необходимое количество парт для учеников третьего класса – {cAnswer}")

