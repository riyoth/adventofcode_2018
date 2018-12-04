from day2 import Day2


def test_part1():
    d = Day2()
    input_1 = []
    input_1.append("abcdef")
    assert (0, 0, 0) == d.part1(input=input_1[0])
    input_1.append("bababc")
    assert (1, 1, 1) == d.part1(input=input_1[1])
    input_1.append("abbcde")
    assert (1, 0, 0) == d.part1(input=input_1[2])
    input_1.append("abcccd")
    assert (0, 1, 0) == d.part1(input=input_1[3])
    input_1.append("aabcdd")
    assert (1, 0, 0) == d.part1(input=input_1[4])
    input_1.append("abcdee")
    assert (1, 0, 0) == d.part1(input=input_1[5])
    input_1.append("ababab")
    assert (0, 1, 0) == d.part1(input=input_1[6])

    assert (4, 3, 12) == d.part1(input='\n'.join(input_1))


def test_part2():
    d = Day2()
    input_2='''abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz'''
    assert 'fgij' == d.part2(input=input_2)
