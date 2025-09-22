from selenium.webdriver.common.by import By
# Кнопки на главной странице
class BUTTON:
    # Кнопка Личный Кабинет
    personal_account_button = (By.XPATH, './/p[text() = "Личный Кабинет"]')
    # Кнопка логотип
    logo_button = (By.XPATH, '//a[@href="/"]')
    # Кнопка Лента заказов
    order_feed_button = (By.XPATH, '//p[text() = "Лента Заказов"]')
    #Кнопка конструктор
    constructor_button = (By.XPATH, '//p[text() = "Конструктор"]')
    #Кнопка "Войти в аккаунт"
    entrance_in_account = (By.XPATH, './/button[text() = "Войти в аккаунт"]')
    #Кнопка "Выйти из аккаунт"
    exit_from_account = (By.XPATH, './/button[text() = "Выход"]')
    #Кнопка "Оформить заказ"
    place_an_order = (By.XPATH, './/button[text() = "Оформить заказ"]')
# Форма входа 
class ENTRANCE:
    # Поле email
    field_email = (By.XPATH, '//input[@name="name"]')
    field_password = (By.XPATH, './/h2[text() = "Вход"]/following::input[@type="password"]')
    # Кнопка войти
    entrance_button1 = (By.XPATH, './/button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa" and text() = "Войти"]')
    # Кнопка зарегестрироваться
    signup = (By.XPATH, './/a[@class="Auth_link__1fOlj" and text()= "Зарегистрироваться"]')
    # Кнопка Восстановить пароль
    restore_password = (By.XPATH, './/a[@class="Auth_link__1fOlj" and text() = "Восстановить пароль"]')
    # Текст "Некорректный пароль"
    invalid_password = (By.XPATH, './/p[text() = "Некорректный пароль"]')
# Форма регестрации
class SIGNUP:
    # Поле имя
    field_name = (By.XPATH, './/label[text() = "Имя"]/following-sibling::input')
    # Поле email
    field_email = (By.XPATH, './/label[text() = "Email"]/following-sibling::input')
    # Поле пароль 
    field_password2 = (By.XPATH, './/label[text() = "Пароль"]/following-sibling::input')
    # Кнопка Зарегестрироваться
    button_signup = (By.XPATH, './/form//button[text()="Зарегистрироваться"]')
    # Кнопка Войти
    entrance_button2 = (By.XPATH, './/a[@class="Auth_link__1fOlj" and text()= "Войти"]')
    # Надпись при дублирование данных при регестрации 
    text_during_dubbing = (By.XPATH, './/p[text()= "Такой пользователь уже существует"]')
# Форма восстановления пароля 
class RESTORE:
    field_email1 = (By.XPATH, './/h2[text() = "Восстановление пароля"]/following::input[@type="text"]')
    button_restore = (By.XPATH, './/h2[text() = "Восстановление пароля"]/following::button[text() = "Восстановить"]')
    entrance_button3 = (By.CLASS_NAME, 'Auth_link__1fOlj' )

#Конструктор 
class KON:
    #Кнопка булки
    button_buns = (By.XPATH, '//span[text()="Булки"]')
    #Кнопка соусы
    button_sauces = (By.XPATH, '//span[text()="Соусы"]')
    #Кнопка начинка
    button_fillings = (By.XPATH, '//span[text()="Начинки"]')
    active_tabl =  (By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc")