def part1(hor_positions):
    n = max(hor_positions)
    used_fuels = [0] * n
    for i in range(n):
        for pos in hor_positions:
            if(pos != i):
                used_fuels[i] += abs(pos - i)
    print("part1: ", min(used_fuels))

def part2(hor_positions):
    n = max(hor_positions)
    used_fuels = [0] * n
    for i in range(n):
        for pos in hor_positions:
            if(pos != i):
                used_fuels[i] += triangular_number(abs(pos - i))
    print("part2: ", min(used_fuels))
            

def triangular_number(n):
    return n * (n + 1) // 2


def main():
    f = open("input7.txt", "r")
    lines = f.readlines()
    f.close()
    data = []
    for line in lines:
        data.append(line.rstrip("\n"))
    hor_positions = []
    for number in data[0].split(','):
        hor_positions.append(int(number))

    part1(hor_positions)
    part2(hor_positions)

if __name__ == "__main__":
    main()