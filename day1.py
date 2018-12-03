class Day1:
    def part1(self, input, separator="\n"):
        total = 0
        for x in input.split(separator):
            total += int(x)

        return total

    def part2(self, input, separator="\n"):
        frequence = {}
        input_list = input.split(separator)
        index = 0
        x = 0
        while True:
            if x in frequence:
                return x
            frequence[x] = 0
            x += int(input_list[index % len(input_list)])
            index += 1


def main():
    d = Day1()
    with open("day1_part1.txt") as day_input:
        data = day_input.read()
    print("Part 1:", d.part1(input=data))
    print("Part 2:", d.part2(input=data))


main()
