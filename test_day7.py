from day7 import Day7


def test_part1():
    d = Day7()
    input_1 = '''Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.'''
    assert "CABDFE" == d.part1(input=input_1)


def test_part2():
    d = Day7()
    input_1 = '''Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.'''
    assert (15, "CABFDE") == d.part2(input=input_1, worker=2, time=0)