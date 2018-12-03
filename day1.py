class Day1:
    def part1(self, input, separator="\n"):
        total = 0
        for x in input.split(separator):
            total += int(x)

        return total

    def part2(self):
        pass


def main():
    d = Day1()
    with open("day1_part1.txt") as day_input:
        data = day_input.read()
    print("Part 1:", d.part1(input=data))


main()
