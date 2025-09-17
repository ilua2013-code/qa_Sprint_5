import pytest
import random
from selenium import webdriver
def generate_email():
    return 'ilya_volkov_31_'+ str(random.randint(100,999)) + '@yandex.ru'

    
def generate_password():
    return str(random.randint(100000,999999))

def generate_name():
    names = ['Иван', 'Алексей', 'Михаил', 'Дмитрий', 'Сергей', 'Андрей', 'Александр']
    return random.choice(names)

def driver():
    return webdriver.Chrome()  