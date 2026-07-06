from pytest_bdd import given, when, then
from apply_discount import apply_discount


@given("que o pedido possui os itens 10, 20, 30 e 30", target_fixture="order_items")
def order_items_quatro():
    return [10.0, 20.0, 30.0, 30.0]


@given("que o pedido possui os itens vazio", target_fixture="order_items")
def order_items_vazio():
    return []


@given("que o pedido possui os itens 10, 20, 30, 30 e 10", target_fixture="order_items")
def order_items_cinco():
    return [10.0, 20.0, 30.0, 30.0, 10.0]


@given("a distancia da entrega é de 15 km", target_fixture="distancia")
def distancia_15km():
    return 15.0


@given("a distancia da entrega é de 10 km", target_fixture="distancia")
def distancia_10km():
    return 10.0


@when("o sistema aplica o desconto", target_fixture="pedido_com_desconto")
def aplica_desconto(total):
    return apply_discount(total)


@then("o resultado com desconto deve ser 87.75")
def check_87_75(pedido_com_desconto):
    assert pedido_com_desconto == 87.75


@then("o resultado com desconto deve ser 0")
def check_zero(pedido_com_desconto):
    assert pedido_com_desconto == 0


@then("o resultado com desconto deve ser 67.5")
def check_67_5(pedido_com_desconto):
    assert pedido_com_desconto == 67.5


@then("o resultado com desconto deve ser 86.0")
def check_86(pedido_com_desconto):
    assert pedido_com_desconto == 86.0
