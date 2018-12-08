from day6 import Day6


def test_part1():
    d = Day6()
    input_1 = '''1, 1
1, 6
8, 3
3, 4
5, 5
8, 9'''
    assert 17 == d.part1(input=input_1, infinity=10)

def test_part2():
    d = Day6()
    input_1 = '''1, 1
1, 6
8, 3
3, 4
5, 5
8, 9'''
    assert 16 == d.part2(input=input_1,size=10, objective=32)