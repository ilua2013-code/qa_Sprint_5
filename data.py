import random


class DATA:
    @staticmethod
    def generate_email():
        return 'ilya_volkov_31_'+ str(random.randint(100,999)) + '@yandex.ru'

    @staticmethod
    def generate_password():
        return str(random.randint(100000,999999))
    @staticmethod
    def generate_name():
        names = ['Иван', 'Алексей', 'Михаил', 'Дмитрий', 'Сергей', 'Андрей', 'Александр']
        return random.choice(names)

