#!/usr/bin/env python3
'''
Template
'''
import sys

with open(sys.argv[1]) as f:
    data = f.readlines()

lines = [line.strip() for line in data]

print(len(lines))

def runpart2(scale):
    _height = len(lines)
    _width = len(lines[0])
    height = _height * scale
    width = _width * scale

    nodes = [[0 for x in range(width)] for y in range(height)]
    for y in range(_height):
        for x in range(_width):
            for _y in range(scale):
                for _x in range(scale):
                    nodes[y + _height * _y][x + _width * _x] = (int(lines[y][x]) + _y + _x + 8) % 9 + 1

    def neighbors(y,x):
        ds = [(-1,0),(1,0),(0,-1),(0,1)]
        for dy,dx in ds:
            if (x + dx) < 0 or (x + dx) >= width or (y + dy) < 0 or (y + dy) >= height: continue
            yield (y+dy,x+dx)

    score = [[-1 for x in range(width)] for y in range(height)]
    print("start")
    score[0][0] = 0
    generations = 0
    while True:
        changed = False
        for y in range(height):
            for x in range(width):
                for _y,_x in neighbors(y,x):
                    if score[_y][_x] == -1:
                        continue
                    cost = nodes[y][x] + score[_y][_x]
                    if score[y][x] == -1 or cost < score[y][x]:
                        score[y][x] = cost
                        changed = True
        generations += 1
        if generations % 10 == 0:
            print(generations,"generations")
        if not changed:
            break
    print(score[height-1][width-1])
    print(generations,"generations total")

runpart2(5)
