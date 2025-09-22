import random


class DATA:
    name = 'Илья'
    password = '123456'
    Email = 'ilya_volkov_31_749@yandex.ru'
    
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
    @staticmethod
    def url():
        #ссылка главной страницы 
        current_url_home_page = 'https://stellarburgers.nomoreparties.site/' 
        #ссылка ленты заказов 
        current_url_order_feed = current_url_home_page + 'feed'
        #ссылка формы регестрации
        current_url_form_signup = current_url_home_page + 'register'
        #ссылка формы восстановления пароля 
        current_url_recovery_password = current_url_home_page + 'forgot-password'
        #ссылка формы входа
        current_url_entrance = current_url_home_page + 'login'
        #ссылка личного кабинета
        current_url_personal_account = current_url_home_page + 'account/profile'