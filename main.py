# Создайте класс, содержащий набор целых чисел. 
# В классе должна быть реализована следующая функциональность:
# ■ Сумма элементов набора.
# ■ Среднеарифметическое элементов набора.
# ■ Максимум из элементов набора.
# ■ Минимум из элементов набора.
# Протестируйте все возможности созданного класса 
# с помощью модульного тестирования(unittest). 


class Numbers:
    def __init__(self, a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def sumNum(self):
        return sum(self.a, self.b, self.c, self.d)

    def sredNum(self):
        return sum(self.a, self.b, self.c, self.d)/4

    def maxNum(self):
        return max(self.a, self.b, self.c, self.d)

    def minNum(self):
        return min(self.a, self.b, self.c, self.d)