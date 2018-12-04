class Day3:
    def parse_input(self, input):
        s = input.split(" ")
        d = {}
        d["id"] = int(s[0][1:])
        d["start"] = int(s[2].split(",")[0]), int(s[2].split(",")[1][:-1])
        d["size"] = int(s[3].split("x")[0]), int(s[3].split("x")[1])
        return d

    def part1(self, input, size=1000, separator="\n"):
        fabric = [[0 for x in range(size)] for y in range(size)]

        for i in input.split(separator):
            r = self.parse_input(i)
            for x in range(r["start"][0], r["start"][0] + r["size"][0]):
                for y in range(r["start"][1], r["start"][1] + r["size"][1]):
                    fabric[x][y] += 1

        overlap = 0
        for x in fabric:
            for y in x:
                if y > 1:
                    overlap += 1
        return overlap

        pass

    def part2(self, input, size=1200, separator="\n"):
        fabric = [[0 for x in range(size)] for y in range(size)]
        id_list = {}
        for x in range(1, len(input.split(separator)) + 1):
            id_list[x] = 0
        for i in input.split(separator):
            r = self.parse_input(i)
            for x in range(r["start"][0], r["start"][0] + r["size"][0]):
                for y in range(r["start"][1], r["start"][1] + r["size"][1]):
                    if fabric[x][y] != 0:
                        id_list[r["id"]] += 1
                        id_list[fabric[x][y]] += 1
                    fabric[x][y] = r["id"]

        for k, v in id_list.items():
            if v == 0:
                return k


def main():
    d = Day3()
    with open("day3_part1.txt") as day_input:
        data = day_input.read()
    print("Part 1:", d.part1(input=data))
    print("Part 2:", d.part2(input=data))


main()
