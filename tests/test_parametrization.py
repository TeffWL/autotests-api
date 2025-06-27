import pytest

@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
# В данном случае в качестве данных используется список с кортежами
def test_several_numbers(number: int, expected: int):
    # Возводим число number в квадрат и проверяем, что оно равно ожидаемому
    assert number ** 2 == expected