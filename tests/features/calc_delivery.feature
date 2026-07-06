Feature: Calculo do total do valor de entrega do pedido
  Como cliente do LocalEats,
  desejo que o sistema calcule o valor da entrega do meu pedido,
  para que eu saiba o valor final da compra.
 
  Scenario: Somar os valores dos itens com a taxa de entrega
    Given que o pedido possui os itens 10, 20 e 30
    And a distancia da entrega é de 15 km
    When o sistema calcula o valor total
    Then o resultado deve ser 67.5

Scenario: Pedido com apenas um item
    Given que o pedido possui apenas o item 45
    And a distancia da entrega é de 10 km
    When o sistema calcula o valor total
    Then o resultado deve ser 50
