def part1(datas):
    x_pos = 0
    depth = 0
    for data in datas:
        words = data.split()
        move = words[0]
        step = int(words[1])
        if(move == "forward"):
            x_pos += step
        elif(move == "down"):
            depth += step
        elif(move == "up"):
            depth -= step
        
    print("part1: ", x_pos * depth)

def part2(datas):
    x_pos = 0
    depth = 0
    aim = 0
    for data in datas:
        words = data.split()
        move = words[0]
        step = int(words[1])
        if(move == "forward"):
            x_pos += step
            depth += aim * step
        elif(move == "down"):
            aim += step
        elif(move == "up"):
            aim -= step
        
    print("part2: ", x_pos * depth)




def main():
   f = open("input2.txt", "r")
   lines = f.readlines()
   f.close()
   data = []
   for line in lines:
      data.append(line.rstrip("\n"))
   
   part1(data)
   part2(data)

if __name__ == "__main__":
    main()