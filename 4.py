def part1(rand_numbers, bingos):
    for rand_number in rand_numbers:
        for bingo in bingos:
            for bingo_line in bingo:
                for bingo_number in bingo_line:
                    if(bingo_number[0] == rand_number):
                        bingo_number[1] = True
                if(checkWin(bingos)):
                    print("rand_number: ", rand_number)
                    return int(rand_number) * sumUnmarkedNumber(bingo)

def part2(rand_numbers, bingos):
    for rand_number in rand_numbers:
        won_bingos = []
        for k, bingo in enumerate(bingos):
            win = False
            for bingo_line in bingo:
                for bingo_number in bingo_line:
                    if(bingo_number[0] == rand_number):
                        bingo_number[1] = True
                        win = checkWin(bingos)
                        if(win):
                            print("Found win in : ")
                            print("rand_number: ", rand_number)
                            print(int(rand_number) * sumUnmarkedNumber(bingo))
                            bingos.remove(bingo)
                            part2(rand_numbers, bingos)
            
def checkWin(bingos):
    #check line
    for bingo in bingos:
        for bingo_line in bingo:
            win = True
            for bingo_number in bingo_line:
                if(bingo_number[1] == False):
                    win = False
            if(win):
                return True
    #check column
    for j in range (0,5):
        column = []
        for bingo in bingos:
            win = True
            for bingo_line in bingo:
                column.append(bingo_line[j][0])
                if(bingo_line[j][1] == False):
                    win = False
            if(win):
                return True
    
def sumUnmarkedNumber(bingo):
    count = 0
    for bingo_line in bingo:
        for bingo_number in bingo_line:
            if(bingo_number[1] == False): 
                count += int(bingo_number[0])
    print("sumUnmarkedNumber: ", count)
    return count

def main():
    f = open("input4.txt", "r")
    lines = f.readlines()
    f.close()
    datas = []
    rand_numbers = lines[0].rstrip("\n").split(",")
    bingos = []
    bingo = []
    for line in lines:
      datas.append(line.rstrip("\n")) 
    for k, line in enumerate(datas): 
        if(k>1): 
            if(line.strip() == "" or k == len(datas)-1):
                bingos.append(bingo)
                bingo = []
            else:
                bingo_line = []
                for number in line.split(" "):
                    if(number.strip() != ""):
                        bingo_line.append([number.strip(), False])
                bingo.append(bingo_line)
    
    print(part1(rand_numbers,bingos))

    #reset
    for bingo in bingos:
        for bingo_line in bingo:
            for bingo_number in bingo_line:
                bingo_number[1] = False
                
    part2(rand_numbers,bingos)

if __name__ == "__main__":
    main()