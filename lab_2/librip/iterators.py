# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.lst = items
        self.index = 0
        self.array = []
        self.bool = 0
        pass

    def __next__(self):
        # Нужно реализовать __next__
        if self.index - 1 == len(self.lst):
            raise StopIteration
        if self.index == len(self.lst):
            self.index += 1
            return self.array
        if self.index == 0:
            self.array.append(self.lst[self.index])
        else:
            k = 0
            while k < len(self.array):
                if self.lst[self.index] == self.array[k]:
                    self.bool += 1
                k += 1
            if self.bool == 0:
                self.array.append(self.lst[self.index])
        self.bool = 0
        self.index += 1
        pass

    def __iter__(self):
        return self
