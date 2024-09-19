import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test_password_lenght():
    """Тест, что длина пароля соответствует заданной """
    password = generate_password(12)
    assert len(password) == 12

def test_password_unique():
    password1 = generate_password(12)
    password2 = generate_password(12)
    assert password1 != password2

"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что два сгенерированных подряд пароля различаются
"""