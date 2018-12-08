from datetime import datetime


class Day4:
    def parse_input(self, input):
        d = datetime.strptime(input[1:17], "%Y-%m-%d %H:%M")
        if input[19] == "f":
            return (d, "f")
        if input[19] == "w":
            return (d, "w")
        if input[19] == "G":
            return (d, input[19:].split(" ")[1][1:])
        return ""

    def part1(self, input, separator="\n"):
        input_list = []
        for x in input.split(separator):
            input_list.append(self.parse_input(x))
        input_list.sort(key=lambda tup: tup[0])

        d = {}
        current_guard = ""
        sleep_minute = 0
        for x in input_list:
            if x[1] == "f":
                sleep_minute = x[0].minute
            elif x[1] == "w":
                for x in range(sleep_minute, x[0].minute):
                    d[(current_guard, x)] += 1
                    d[(current_guard, "total")] += 1
            else:
                current_guard = x[1]
                if (x[1], 0) not in d:
                    d.update({(x[1], k): 0 for k in range(59)})
                    d[(x[1], "total")] = 0

        most_sleep = 0
        guard = 0
        slept_minute = {}
        result = (0, 0, 0)
        for k, v in d.items():
            if k[1] == "total" and v > most_sleep:
                most_sleep = v
                guard = k[0]
            if k[1] != "total":
                if k[0] not in slept_minute:
                    slept_minute[k[0]] = (k[1], v)
                if v > slept_minute[k[0]][1]:
                    slept_minute[k[0]] = (k[1], v)

        return (guard, slept_minute[guard][0], int(guard) * slept_minute[guard][0])

    def part2(self, input, separator="\n"):
        input_list = []
        for x in input.split(separator):
            input_list.append(self.parse_input(x))
        input_list.sort(key=lambda tup: tup[0])

        d = {}
        current_guard = ""
        sleep_minute = 0
        for x in input_list:
            if x[1] == "f":
                sleep_minute = x[0].minute
            elif x[1] == "w":
                for x in range(sleep_minute, x[0].minute):
                    d[(current_guard, x)] += 1
                    d[(current_guard, "total")] += 1
            else:
                current_guard = x[1]
                if (x[1], 0) not in d:
                    d.update({(x[1], k): 0 for k in range(59)})
                    d[(x[1], "total")] = 0

        most_sleep = 0
        guard = 0
        for k, v in d.items():
            if k[1] != "total" and v > most_sleep:
                guard = k[0]
                minute = k[1]
                most_sleep = v

        return (guard, minute, int(guard) * minute)


def main():
    d = Day4()
    with open("day4_part1.txt") as day_input:
        data = day_input.read()
    print("Part 1:", d.part1(input=data))
    print("Part 2:", d.part2(input=data))


main()
