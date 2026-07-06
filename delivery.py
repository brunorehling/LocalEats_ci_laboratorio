

def calculate_delivery(items: list[float], distance: float) -> float:
    delivery_tax : float = 0

    delivery_value = distance * 0.5
    if delivery_value > 2 and len(items) > 0 :
        delivery_tax = delivery_value

    return sum(items, delivery_tax)