from delivery import calculate_delivery 

def apply_discount(total: calculate_delivery) -> float:
    if total >= 100:
        discount_percent = 0.80
        return total * discount_percent
    elif total >= 80:
        discount_percent = 0.90
        return total * discount_percent
    return total
    ...
