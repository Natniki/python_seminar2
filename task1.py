#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, 
#чтобы все монетки были повернуты вверх одной и той же стороной.
#Выведите минимальное количество монет, которые нужно перевернуть

N = int(input("Введите количество монет: "))

count = 0

for i in range(N):

    a = int(input("Введите значение 0,если орел. И значение 1,если решка: "))

    if a != 1 and a != 0:

        print("errorrrr!")

    else:

        if a == 1:

            count = count + 1

print(count)