from pprint import pprint
import math
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

@dataclass
class Vector:
    a: Point
    b: Point

def part1(datas):
    vectors = []
    for data in datas:
        spl = data.split(' -> ')
        p1 = spl[0].split(',')
        p2 = spl[1].split(',')
        a = Point(int(p1[0]), int(p1[1]))
        b = Point(int(p2[0]), int(p2[1]))
        vectors.append(Vector(a,b))

    max_n = 0
    for vector in vectors:
            if(vector.a.x > max_n):
                max_n = vector.a.x
            if(vector.a.y > max_n):
                max_n = vector.a.y
            if(vector.b.x > max_n):
                max_n = vector.b.x
            if(vector.b.y > max_n):
                max_n = vector.b.y
    field = [[0 for x in range(max_n+1)] for y in range(max_n+1)] 

    for i in range (0, max_n-1):
        for j in range(0, max_n-1):
            field[i][j] = 0


    for vector in vectors:
        print(vector)
        if(vector.a.y == vector.b.y ):
            for i in range(min(vector.a.x, vector.b.x), max(vector.a.x, vector.b.x)+1):
                field[vector.a.y][i] += 1
        if(vector.a.x == vector.b.x):
            for j in range(min(vector.a.y,vector.b.y), max(vector.a.y,vector.b.y)+1):
                field[j][vector.a.x] += 1
    count=0
    for f in field:
        for g in f:
            if(g>=2): count +=1
    print(count)

def part2(datas):
    vectors = []
    for data in datas:
        spl = data.split(' -> ')
        p1 = spl[0].split(',')
        p2 = spl[1].split(',')
        a = Point(int(p1[0]), int(p1[1]))
        b = Point(int(p2[0]), int(p2[1]))
        vectors.append(Vector(a,b))

    max_n = 0
    for vector in vectors:
            if(vector.a.x > max_n):
                max_n = vector.a.x
            if(vector.a.y > max_n):
                max_n = vector.a.y
            if(vector.b.x > max_n):
                max_n = vector.b.x
            if(vector.b.y > max_n):
                max_n = vector.b.y
    field = [[0 for x in range(max_n+1)] for y in range(max_n+1)] 

    for i in range (0, max_n-1):
        for j in range(0, max_n-1):
            field[i][j] = 0


    for vector in vectors:
        print(vector)
        if(vector.a.y == vector.b.y ):
            for i in range(min(vector.a.x, vector.b.x), max(vector.a.x, vector.b.x)+1):
                field[vector.a.y][i] += 1
        elif(vector.a.x == vector.b.x):
            for j in range(min(vector.a.y,vector.b.y), max(vector.a.y,vector.b.y)+1):
                field[j][vector.a.x] += 1
        else:
            if(vector.a.x<vector.b.x):
                inc_i = +1
            else:
                inc_i = -1

            if(vector.a.y<vector.b.y):
                inc_j = +1
            else:
                inc_j = -1

            i = vector.a.x
            j = vector.a.y
            field[j][i] += 1
            go = True
            while go:
                print(i, j)
                i += inc_i
                j += inc_j
                field[j][i] += 1
                if (i == vector.b.x and j == vector.b.y): go = False

    count=0
    for f in field:
        for g in f:
            if(g>=2): count +=1
    pprint(field)
    print(count)
            
    




def main():
   f = open("input5.txt", "r")
   lines = f.readlines()
   f.close()
   datas = []
   for line in lines:
      datas.append(line.rstrip("\n"))
   
   #part1(datas)
   part2(datas)

if __name__ == "__main__":
    main()