from delivery import calculate_delivery

def test_calculate_delivery():
    assert calculate_delivery([10, 20, 30], 15) == 63