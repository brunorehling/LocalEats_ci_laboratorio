from apply_discount import apply_discount
from delivery import calculate_delivery


def test_apply_discount_80():
    pedido = calculate_delivery([10.0, 20.0, 30.0, 30.0], 15.0)
    assert apply_discount(pedido) == 87.75


def test_apply_discount_100():
    pedido = calculate_delivery([10.0, 20.0, 30.0, 30.0, 10.0], 15.0)
    assert apply_discount(pedido) == 86


def test_apply_discount_pedido_vazio():
    pedido = calculate_delivery([], 10)
    assert apply_discount(pedido) == 0


def test_apply_discount_pedido_nao_atingiu_valor_minimo():
    pedido = calculate_delivery([10.0, 20.0, 30.0], 15.0)
    assert apply_discount(pedido) == 67.5