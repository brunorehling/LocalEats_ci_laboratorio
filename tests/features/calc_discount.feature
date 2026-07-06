Feature: Aplicacao de desconto para pedidos acima de R$80
  Como cliente do LocalEats,
  desejo receber um desconto quando o valor do meu pedido ultrapassar R$80,
  para pagar um valor menor em compras de maior valor.

  Scenario: Pedido entre 80 e 100 recebe desconto de 10%
    Given que o pedido possui os itens 10, 20, 30 e 30
    And a distancia da entrega é de 15 km
    When o sistema calcula o valor total
    And o sistema aplica o desconto
    Then o resultado com desconto deve ser 87.75

  Scenario: Pedido vazio nao recebe desconto
    Given que o pedido possui os itens vazio
    And a distancia da entrega é de 10 km
    When o sistema calcula o valor total
    And o sistema aplica o desconto
    Then o resultado com desconto deve ser 0

  Scenario: Pedido abaixo do valor minimo nao recebe desconto
    Given que o pedido possui os itens 10, 20 e 30
    And a distancia da entrega é de 15 km
    When o sistema calcula o valor total
    And o sistema aplica o desconto
    Then o resultado com desconto deve ser 67.5

  Scenario: Pedido acima de 100 recebe desconto de 20%
    Given que o pedido possui os itens 10, 20, 30, 30 e 10
    And a distancia da entrega é de 15 km
    When o sistema calcula o valor total
    And o sistema aplica o desconto
    Then o resultado com desconto deve ser 86.0