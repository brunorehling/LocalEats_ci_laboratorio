import pytest
from delivery import calculate_delivery


def test_calculate_delivery():
    assert calculate_delivery([10.0, 20.0, 30.0], 15.0) == 67.5


def test_calculate_delivery_lista_vazia():
    assert calculate_delivery([], 10) == 0


@pytest.mark.xfail(reason="Bug conhecido: aceita valores negativos silenciosamente (ver Issue #X)")
def test_calculate_delivery_valores_negativos():
    resultado = calculate_delivery([-10, 20, 30], 15)
    assert resultado == 47.5


@pytest.mark.xfail(raises=TypeError,
                   reason="Bug conhecido: nao valida tipo dos itens (ver Issue #X)")
def test_calculate_delivery_com_string():
    calculate_delivery(['abc', 20, 30], 15)
