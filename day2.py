class Day2:
    def part1(self, input, separator="\n"):
        global_count = {}
        global_count[2] = 0
        global_count[3] = 0
        for x in input.split("\n"):
            local_count = {}
            local_count[2] = 0
            local_count[3] = 0
            for c in x:
                if x.count(c) == 2:
                    local_count[2] = 1
                if x.count(c) == 3:
                    local_count[3] = 1
            if local_count[2] >= 1:
                global_count[2] += 1
            if local_count[3] >= 1:
                global_count[3] += 1

        return (global_count[2], global_count[3], global_count[2] * global_count[3])

    def part2(self, input, separator="\n"):
        list_input = input.split()
        result = {}

        for x in range(len(list_input[0])):
            result[x] = []

        for i,x in enumerate(list_input):
            for y in list_input[i+1:]:
                cpt = 0
                temp = ""
                for cx, cy in zip(x, y):
                    if cx == cy:
                        cpt += 1
                        temp += cx
                if cpt >= len(x) - 1:
                    return temp


def main():
    d = Day2()
    with open("day2_part1.txt") as day_input:
        data = day_input.read()
    print("Part 1:", d.part1(input=data))
    print("Part 2:", d.part2(input=data))

main()
