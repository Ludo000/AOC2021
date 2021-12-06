def part1(fishs):
    curr_len = len(fishs)
    days = 80
    for i in range(0, days):
        for k in range(0, curr_len):
            if( fishs[k] == 0):
                fishs[k] = 6
                fishs.append(8)
                curr_len +=1
            else:
                fishs[k] -= 1
    print("part1: ", len(fishs))

def part2(fishs):
    stock_fish = [0 for x in range(0, 9)]
    for fish in fishs:
        stock_fish[fish] += 1
    
    for i in range(0, 256):
        print(stock_fish)
        zero_count_fish = stock_fish[0]
        # 2 => 1, ... so count(2) => count(1), ... so stock_fish[2] => stock_fish[1], ...
        for k in range(0, 8):
            stock_fish[k] = stock_fish[k+1]
        stock_fish[8] = zero_count_fish
        # all 0s becomes 6s
        stock_fish[6] += zero_count_fish
    result = sum(stock_fish)
    print("part2: ", result)        

def main():
    f = open("input6.txt", "r")
    lines = f.readlines()
    f.close()
    datas = []
    for line in lines:
        datas.append(line.rstrip("\n"))
    fishs = []
    for data in datas:
        for number in data.split(','):
            fishs.append(int(number))

    #part1(fishs)
    part2(fishs)

if __name__ == "__main__":
    main()