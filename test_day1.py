from day1 import Day1


def test_part1():
    d = Day1()
    input_1 = '+1, -2, +3, +1'
    assert 3 == d.part1(input=input_1, separator=',')

    input_2 = '+1, +1, +1'
    assert 3 == d.part1(input=input_2, separator=',')
    input_3 = '+1, +1, -2'
    assert 0 == d.part1(input=input_3, separator=',')
    input_4 = '-1, -2, -3'
    assert -6 == d.part1(input=input_4, separator=',')


def test_part2():
    d = Day1()
    input_1 = '+1, -1'
    assert 0 == d.part2(input=input_1, separator=',')
    input_2 = '+3, +3, +4, -2, -4'
    assert 10 == d.part2(input=input_2, separator=',')
    input_3 = '-6, +3, +8, +5, -6'
    assert 5 == d.part2(input=input_3, separator=',')
    input_4 = '+7, +7, -2, -7, -4'
    assert 14 == d.part2(input=input_4, separator=',')
