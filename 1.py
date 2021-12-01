def part1(datas):
    count = 0
    for k, data in enumerate(datas):
        if(k>0 and datas[k-1]<datas[k]):
            count += 1
    print(count)

def part2(datas):
    count = 0
    prev_sum = 0
    for k, data in enumerate(datas):
        if(k>2):
            curr_sum = datas[k-2]+datas[k-1]+datas[k]
            if(prev_sum < curr_sum):
                count += 1
            prev_sum = curr_sum
    print(count-1)




def main():
   f = open("input1.txt", "r")
   lines = f.readlines()
   f.close()
   data = []
   for line in lines:
      data.append(int(line.rstrip("\n")))
   
   part1(data)
   part2(data)

if __name__ == "__main__":
    main()