from day3 import Day3


def test_parse():
    d = Day3()
    t = """#1 @ 1,3: 4x4"""
    result = {}
    result["id"] = 1
    result["start"] = (1, 3)
    result["size"] = (4, 4)
    assert result == d.parse_input(t)


def test_part1():
    d = Day3()
    t = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""
    assert 4 == d.part1(t)


def test_part2():
    d = Day3()
    t = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""
    assert 3 == d.part2(t)
    
