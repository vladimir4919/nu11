import random

class Bag:

    def __init__(self):
        self.samples = [i for i in range(1, 91)]
    #достаем бочонок с номером из мешочка
    def select_sample(self):
        return self.samples.pop(random.randrange(len(self.samples)))



"""карточка игрока,заполнена цифрами в три  строки по пять в каждой
#цифры в карточке не повторяются,и расположены по возрастанию в строке"""

class Ticket:
    def __init__(self):
        self.numbers = []
        while len(self.numbers) < 15:
            i = random.randrange(1, 91)
            if i not in self.numbers:
                self.numbers.append(i)
        self.strings = {}
        for i in range(3):
            self.strings[i] = self.numbers[i*5:i*5 + 5]
            self.strings[i].sort()

#Изображение карточки
    def show_ticket(self, num):
        print('Номер на карточке игрока: ', num)
        print("-"*30)
        for i in range(3):
            for num in self.strings[i]:
                print(num, " ", end=" ")
            print("\n")
        print("-" * 30)


    """  метод __str__  """

    def __str__(self):
        return f'количество строк в карте {len(self.strings)}'




    def __ne__(self, other):
        """
        сравниваем длину и число строк
        """

        return len(self.numbers) != len(self.strings)




    def __eq__(self, other):
        """
        сравниваем длину строк карточки
        """
        string2 = len(self.strings[1])
        string1 = len(self.strings[0])
        return string1 == string2

    def __getitem__(self, item):
        """
        смотрим элементы карточки
        """
        return self.numbers[item]


class Gamer:
    def __init__(self):
        self.card = Ticket()

    def is_victory(self):
        for i in range(3):
            if self.card.strings[i].count("-") < 5:
                return False
        return True

    def __str__(self):
        pass




class Dropout(Gamer):
    def act(self, num):
        pass





class Person(Gamer):
    def act(self, num):
        self.card.show_ticket(num)
        replay = None
        while replay not in ['yes', 'no']:
            replay = input("Зачеркнуть номер? (yes/no) ")
        if replay == "yes":
            if num not in self.card.numbers:
                print("Такого номера  на Вашей карточке нет ! ")
                return False
            else:
                for i in range(3):
                    if num in self.card.strings[i]:
                        self.card.strings[i][self.card.strings[i].index(num)] = '-'
                        self.card.numbers.pop(self.card.numbers.index(num))
                        return True
        else:
            if num in self.card.numbers:
                print("Такой номер  есть на Вашей карточке есть! ")
                return False
            return True

     def __str__(self):
        return f'Игрок человек - осталось {len(self.card.numbers)} номеров'

    def __eq__(self, other):
        """
        сравниваем число зачеркнутых номеров
        """
        stroke_01 = self.card.numbers.count('-')
        stroke_02 = other.card.numbers.count('-')
        return stroke_01 == stroke_02

    def __ne__(self, other):
        """
        сравниваем число зачеркнутых номеров
        """
        stroke_01 = self.card.numbers.count('-')
        stroke_02 = other.card.numbers.count('-')
        return stroke_01 != stroke_02


class Computer(Gamer):
    def act(self, num):
        self.card.show_ticket(num)
        if num in self.card.numbers:
            for i in range(3):
                if num in self.card.strings[i]:
                    self.card.strings[i][self.card.strings[i].index(num)] = '-'
                    self.card.numbers.pop(self.card.numbers.index(num))
        return True


    def __str__(self):
        return f'Игрок компьютер - остались номера {self.card.numbers}'

    def __eq__(self, other):
        """
        сравниваем число зачеркнутых номеров
        """
        progress01 = self.card.numbers.count('-')
        progress02 = other.card.numbers.count('-')
        return progress01 == progress02

    def __ne__(self, other):
        """
        сравниваем число зачеркнутых номеров
        """
        progress_1 = self.card.numbers.count('-')
        progress_2 = other.card.numbers.count('-')
        return progress_2 != progress_1

if __name__ == '__main__':
    import unittest

    class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Ticket()

    def tearDown(self):
        pass

    def test_str(self):
        self.assertEqual(len(self.card.strings), 3)
        self.assertEqual(len(self.card.numbers), 15)

    def test_eq(self):
        string01 = len(self.card.strings[0])
        string02 = len(self.card.strings[1])
        assert string01 == string02