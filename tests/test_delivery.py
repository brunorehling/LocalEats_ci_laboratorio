from delivery import calculate_delivery

def test_calculate_delivery():
    assert calculate_delivery([10.0, 20.0, 30.0], 15.0) == 67.5