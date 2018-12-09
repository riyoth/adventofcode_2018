class Day7:
    def parse(self, input):
        s = input.split(" ")
        return (s[7], s[1])

    def part1(self, input, separator="\n"):
        d = {}
        for x in input.split(separator):
            r = self.parse(x)
            if r[0] not in d:
                d[r[0]] = []
            if r[1] not in d:
                d[r[1]] = []
            d[r[0]].append(r[1])

        done = []
        while len(d) > 0:
            for k in sorted(d):
                if set(d[k]).issubset(done):
                    done.append(k)
                    del d[k]
                    break

        return "".join(done)

    def part2(self, input, worker=5, time=60, separator="\n"):
        d = {}
        for x in input.split(separator):
            r = self.parse(x)
            if r[0] not in d:
                d[r[0]] = []
            if r[1] not in d:
                d[r[1]] = []
            d[r[0]].append(r[1])

        done = []
        tasks = []
        workers = [x for x in range(worker)]
        timer =-1 
        while len(d) > 0 or len(tasks) > 0:
            timer += 1
            x = len(tasks) -1

            while x >= 0:
                tasks[x] = (tasks[x][0], tasks[x][1], tasks[x][2] - 1)
                if tasks[x][2] == 0:
                    done.append(tasks[x][0])
                    workers.append(tasks[x][1])
                    tasks.pop(x)
                x -= 1

            for k in sorted(d):
                if set(d[k]).issubset(done) and len(workers) > 0:
                    tasks.append((k, workers.pop(), time + ord(k.lower()) - 96))
                    del d[k]
            
        return (timer, ''.join(done))


def main():
    d = Day7()
    with open("day7_part1.txt") as day_input:
        data = day_input.read()
    print("Part 1:", d.part1(input=data))
    # not IOXZFSWAJPEQDUVLNYMHTBCRGK
    print("Part 2:", d.part2(input=data))


if __name__ == "__main__":
    main()
