# '''Напишите 3 функции

# 1-ая должна принимать список. Добавлять в этот список элементы
# 'Element', 'start', 'finish'. Все элементы первоначального списка должны находиться  между элементами 'start', 'finish''''

my_set = {4, 7, 8, 0}

# for element in my_set:
#     print(element + 8)

my_tuple = ("hello", "5", "John")

for element in my_tuple:
    print("Element, ","start" ,+ element +, "finish")

for index in range(len(my_tuple)):
    print("Element, ","start" ,+ my_tuple[index] + ,"finish")
