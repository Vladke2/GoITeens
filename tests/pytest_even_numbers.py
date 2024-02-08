from .even_numb import even_numbers


def test_even_number():
    result = even_numbers(2)
    assert result == 'Число парне'
    assert result != 'Число не парне'
    assert isinstance(result, str)


def test_even_number_5():
    result = even_numbers(5)
    assert result == 'Число не парне'
    assert result != 'Число парне'
    assert isinstance(result, str)


def test_even_number_223322():
    result = even_numbers(223322)
    assert result == 'Число парне'
    assert result != 'Число не парне'
    assert isinstance(result, str)
