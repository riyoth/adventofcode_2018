from day5 import Day5


def test_part1():
    d = Day5()
    input_1 = 'aA'
    assert 0 == d.part1(input_1)
    input_2 = 'abBA'
    assert 0 == d.part1(input_2)
    input_3 = 'abAB'
    assert 4 == d.part1(input_3)
    input_4 = 'aabAAB'
    assert 6 == d.part1(input_4)


def test_part2():
    d = Day5()
    input_1 = 'dabAcCaCBAcCcaDA'
    assert 4 == d.part2(input_1)
    pass
