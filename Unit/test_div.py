import pytest

from Unit.div import div


@pytest.mark.happy
@pytest.mark.parametrize
def test_div_int():
    assert div(10, 5) == 2
    assert div(10, 2) == 5
    assert div(10000000, 1) == 10000000


@pytest.mark.happy
@pytest.mark.parametrize("number1,number2,expectation", {
    (10, 2, 5),
    (10, 5, 2),
    (1000000, 1, 1000000)
})
def test_div_int(number1, number2, expectation):
    assert div(number1, number2) == expectation


def test_div_float():
    assert div(10, 3) == 3.33
    assert div(10.2, 0.2) == 51


@pytest.mark.expection
def test_div_expection():
    assert div(10, 'a')
    assert div('avc', 10)


@pytest.mark.expection
def test_div_zero():
    '''
    对于除零异常的报错处理
    '''
    with pytest.raises(ZeroDivisionError):
        div(10, 0)
