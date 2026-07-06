

def calculate_delivery(items: list[float], distance: float) -> float:
    for item in items:
        if not isinstance(item, (int, float)):
            raise TypeError(f"Item inválido: {item!r} não é um número")
        if item < 0:
            raise ValueError(f"Item inválido: valor negativo não permitido ({item})")

    delivery_tax: float = 0
    delivery_value = distance * 0.5
    if delivery_value > 2 and len(items) > 0:
        delivery_tax = delivery_value

    return sum(items, delivery_tax)
