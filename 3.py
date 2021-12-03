def part1(datas):
    i=0
    gamma = ""
    epsilon = ""
    if(len(datas) <= 0): return
    for i in range(0, len(datas[0])):
        column = []
        for line in datas:
            curr_bit = line[i]
            column.append(curr_bit)
        if(column.count("1") > column.count("0")):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    print("result part1: ", int(gamma, base=2) * int(epsilon, base=2))

def part2(datas, mode, i):
    if(len(datas) <= 0): return
    if(len(datas) == 1): 
        print("part2 ", mode, ": ", int(datas[0], base=2))
        return int(datas[0], base=2)
    column = []
    for line in datas:
        curr_bit = line[i]
        column.append(curr_bit)
    if(mode == "oxygen") :
        bit_criteria = "1"
        if(column.count("0") > column.count("1")):
            bit_criteria = "0"
    else :
        bit_criteria = "0"
        if(column.count("0") > column.count("1")):
            bit_criteria = "1"
    new_datas = []
    for data in datas:
        if(data[i] == bit_criteria):
            new_datas.append(data)
    part2(new_datas, mode, i + 1)   



        





def main():
   f = open("input3.txt", "r")
   lines = f.readlines()
   f.close()
   data = []
   for line in lines:
      data.append(line.rstrip("\n"))
   
   part1(data)
   part2(data, "oxygen", 0)
   part2(data, "co2", 0)

if __name__ == "__main__":
    main()