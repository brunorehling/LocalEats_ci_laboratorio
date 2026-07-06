from pytest_bdd import given, when, then
from delivery import calculate_delivery


@given("que o pedido possui os itens 10, 20 e 30", target_fixture="order_items")
def order_items():
    return [10, 20, 30]


@given("a distancia da entrega é de 15 km", target_fixture="distancia")
def distancia_15km():
    return 15


@given("que o pedido possui apenas o item 45", target_fixture="order_items")
def order_item_unico():
    return [45]


@given("a distancia da entrega é de 10 km", target_fixture="distancia")
def distancia_10km():
    return 10


@when("o sistema calcula o valor total", target_fixture="total")
def calculate(order_items, distancia):
    return calculate_delivery(order_items, distancia)


@then("o resultado deve ser 67.5")
def check_total_67_5(total):
    assert total == 67.5


@then("o resultado deve ser 50")
def check_total_50(total):
    assert total == 50
