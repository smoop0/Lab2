import Lab2 as lab2

def test_find_min_max():
    result = []
    input_arr = [12, 32, 4, 123, 7]
    test_arr = [4, 123]

    result = lab2.find_min_max(input_arr)

    assert (result == test_arr)

def test_calc_average():
    result = []
    input_arr = [12, 32, 4, 123, 7]
    test = 35.6

    result = lab2.calc_average(input_arr)

    assert (result == test)

def test_calc_median_temperature():
    result = []
    input_arr = [12, 32, 4, 123, 7]
    test = 12

    result = lab2.calc_median_temperature(input_arr)

    assert (result == test)