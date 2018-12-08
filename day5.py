import string

class Day5:
    def part1(self, input, separator="\n"):
        s = input
        x = len(s)-1
        while x >= 1 :
            if (
                s[x].isupper() != s[x -1].isupper()
                and s[x].lower() == s[x - 1].lower()
            ):
                s = s[:x - 1] + s[x+1:]
                x = len(s)-1
            else:
                x -= 1

        return len(s)

    def part2(self, input, separator="\n"):
        letters = list(string.ascii_lowercase)
        result = 10000000
        for x in letters:
            t = str.maketrans('', '', x+x.upper())
            r = self.part1(input=input.translate(t))
            if r < result:
                result = r
        return result


def main():
    d = Day5()
    with open("day5_part1.txt") as day_input:
        data = day_input.read()
    print("Part 1:", d.part1(input=data))
    print("Part 2:", d.part2(input=data))


if __name__ == "__main__":
    main()
