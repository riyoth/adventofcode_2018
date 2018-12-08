import math


class Day6:
    def print_grid(self,grid):
        high =[0,0]
        low =[0,0]
        for k,v in grid.items():
            if k[0] > high[0]:
                high[0] = k[0]
            if k[0] < low[0]:
                low[0] = k[0]
            if k[1] > high[1]:
                high[1] = k[1]
            if k[1] < low[1]:
                low[1] = k[1]
        
        for y in range(low[0], high[0]):
            current_line = ''
            for x in range(low[1], high[1]):
                if (x,y) in grid:
                    current_line += str(grid[(x,y)][0])
                else:
                    current_line += '#'
            print(current_line)

    def part1(self, input, infinity=400, separator="\n"):
        grid = {}

        for i, j in enumerate([(int(x.split(',')[0]), int(x.split(',')[1])) for x in input.split(separator)]):
            for x in range(infinity*-1, infinity):
                for y in range(infinity*-1, infinity):
                    distance = abs(x)+abs(y)
                    if (j[0]+x, j[1]+y) not in grid or grid[(j[0]+x, j[1]+y)][1] > distance:
                        grid[(j[0]+x, j[1]+y)] = (i, distance)
                    elif grid[(j[0]+x, j[1]+y)][1] == distance:
                        grid[(j[0]+x, j[1]+y)] = (-1, distance)

        result = {}
        to_infinity = []
        for k, x in grid.items():
            if x[0] not in result:
                result[x[0]] = 0
            result[x[0]] += 1
            if x[1] == infinity:
                to_infinity.append(x[0])

        winners = (-1, 0)
        for k, v in result.items():
            if k not in to_infinity and v > winners[1]:
                winners = (k, v)
        return winners[1]


    def part2(self, input, size=500, objective=10000, separator="\n"):
        safe_area = 0

        for x in range(size):
            for y in range(size):
                total_distance = 0
                for i in [(int(x.split(',')[0]), int(x.split(',')[1])) for x in input.split(separator)]:
                    total_distance += abs(x-i[0])+abs(y-i[1])
                if total_distance < objective:
                    safe_area +=1
                    

        return safe_area


def main():
    d = Day6()
    with open("day6_part1.txt") as day_input:
        data = day_input.read()
    print("Part 1:", d.part1(input=data))
    print("Part 2:", d.part2(input=data))


if __name__ == "__main__":
    main()
