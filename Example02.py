# 1. За день машина проезжает n километров. 
# Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

# **Input:**

# n = 700

# m = 750

# **Output:**

print(f"Введите кол-во километров, которое машина проезжает за день")
n = int(input())

print(f"Введите длину машрута в километрах")
m = int(input())

d = int(m/n)

print(f"Сколько дней машине нужно на преодаление маршрута? – Ответ: {d}")


