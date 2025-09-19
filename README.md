QA Automation Project: Stellar Burgers
Описание
Автоматизированные тесты для веб-приложения "Stellar Burgers" (аналог Burger King). Проект включает тестирование функциональности регистрации, авторизации, личного кабинета и конструктора бургеров.
Технологии

Pytest - фреймворк для тестирования

Selenium WebDriver - автоматизация браузера



Структура проекта
text
qa_5print_5/
├── fixtures.py              # Фикстуры Pytest
├── locators.py              # Локаторы элементов
├── tests/                   # Тестовые сценарии
│   ├── registration/        # Тесты регистрации
│   │   ├── test1_successful_registration.py
│   │   ├── test2_none_password.py
│   │   ├── test3_none_name.py
│   │   ├── test4_none_email.py
│   │   ├── test5_invalid_password_len_5.py
│   │   └── test6_registration_with_the_same_data.py
│   ├── authorization/       # Тесты авторизации
│   │   ├── test7_invalid_email.py
│   │   ├── test8_entrance_button_in_form_registration.py
│   │   ├── test9_entrance_button_in_form_restore_pass.py
│   │   ├── test10_entrance_button_Login_to_account.py
│   │   └── test11_entrance_button_personal_account.py
│   ├── personal_account/    # Тесты личного кабинета
│   │   ├── test12_transition_from_your_personal_account_to_the_designer.py
│   │   ├── test13_transition_personal_account.py
│   │   ├── test14_Click_on_the_Stellar_Burgers_lc.py
│   │   └── test15_testing_exit_button.py
│   └── constructor/         # Тесты конструктора
│       ├── test16_button_buns.py
│       ├── test17_button_sauces.py
│       └── test18_button_fillings.py
├── .gitignore               # Исключения для Git
└── README.md               # Документация
Тестовые сценарии
Регистрация
Успешная регистрация - позитивный сценарий

Регистрация без пароля - негативный сценарий

Регистрация без имени - негативный сценарий

Регистрация без email - негативный сценарий

Невалидный пароль (5 символов) - проверка валидации

Регистрация с существующими данными - проверка уникальности

Авторизация
Невалидный email - проверка формата email
8-11. Тесты кнопок входа - различные способы авторизации

Личный кабинет
12-15. Навигация и функциональность - переходы и выход из системы

Конструктор бургеров
16-18. Переключение разделов - булки, соусы, начинки