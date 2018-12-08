from day4 import Day4
from datetime import datetime


def test_parse():
    d = Day4()
    input_1 = "[1518-11-01 00:25] wakes up"
    r = (datetime(year=1518, month=11, day=1, hour=0, minute=25), 'w')
    assert r == d.parse_input(input=input_1)
    input_2 = "[1518-11-01 00:05] falls asleep"
    r = (datetime(year=1518, month=11, day=1, hour=0, minute=5), 'f')
    assert r == d.parse_input(input=input_2)
    input_3 = "[1518-11-01 23:58] Guard #99 begins shift"
    r = (datetime(year=1518, month=11, day=1, hour=23, minute=58), '99')
    assert r == d.parse_input(input=input_3)


def test_part1():
    d = Day4()
    input_1 = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""
    assert ('10', 24, 240) == d.part1(input_1)


def test_part2():
    d = Day4()
    input_1 = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""
    assert ('99', 45, 4455) == d.part2(input_1)
