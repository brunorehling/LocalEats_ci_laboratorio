from delivery import calculate_delivery


def test_calculate_delivery():
    assert calculate_delivery([10.0, 20.0, 30.0], 15.0) == 67.5


def test_calculate_delivery_lista_vazia():
    assert calculate_delivery([], 10) == 0

