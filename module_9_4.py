from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'
lam_func = list(map(lambda x, y: x == y, first, second))
print(lam_func)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "w", encoding='utf-8') as file:
            for line in data_set:
                file.write(f"{line}\n")

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *word):
        self.word = word

    def __call__(self):
        return choice(self.word)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
