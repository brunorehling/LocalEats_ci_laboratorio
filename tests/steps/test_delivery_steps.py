from pytest_bdd import given, when, then
from delivery import calculate_delivery
 
 
@given("que o pedido possui os itens 10, 20 e 30", target_fixture="order_items")
def order_items():
    return [10, 20, 30]
 
@given("a distancia da entrega é de 15 km", target_fixture="distancia")
def distancia():
    return 15

@when("o sistema calcula o valor total", target_fixture="total")
def calculate(order_items, distancia):
    return calculate_delivery(order_items, distancia)
 
@then("o resultado deve ser 67.5")
def check_total(total):
    assert total == 67.5
