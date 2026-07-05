

def calculate_delivery(items, distance):
    delivery_tax = 0

    delivery_value = distance * 0.2
    if delivery_value > 2 :
        delivery_tax = delivery_value

    return sum(items, delivery_tax)