#!/usr/bin/env python3
'''
Template
'''
import sys

with open(sys.argv[1]) as f:
    data = f.readlines()

lines = [line.strip() for line in data]

print(len(lines))

height = len(lines)
width = len(lines[0])

def neighbors(coord):
    y,x = coord
    ds = [(-1,0),(1,0),(0,-1),(0,1)]
    for dy,dx in ds:
        if (x + dx) < 0: continue
        if (x + dx) >= width * 5: continue
        if (y + dy) < 0: continue
        if (y + dy) >= height * 5: continue
        yield (y+dy,x+dx)

nodes = {}
for y in range(height):
    for x in range(width):
        for _y in range(5):
            for _x in range(5):
                nodes[(y + height * _y, x + width * _x)] = (int(lines[y][x]) + _y + _x + 8) % 9 + 1

for y in range(height*5):
    for x in range(width*5):
        print(nodes[(y,x)],end='')
    print()

def findMin(Q,dist):
    found = None
    for n in Q:
        if found is None or dist[n] < dist[found]:
            found = n
    return found

target = (height * 5 - 1, width * 5 - 1)

import math

def dijkstraThisShit(nodes, src):
    Q = set()
    dist = {}
    prev = {}
    for node in nodes.keys():
        dist[node] = 10000000000000.0
        prev[node] = None
        Q.add(node)
    dist[src] = 0
    while Q:
        u = findMin(Q,dist)
        if u == target:
            break
        Q.remove(u)
        for v in neighbors(u):
            if v not in Q: continue
            alt = dist[u] + nodes[v] # weight is on the node itself
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    return dist, prev

dist, prev = dijkstraThisShit(nodes, (0,0))

s = []
u = target
while u is not None:
    s.append(u)
    u = prev[u]

print(nodes[(0,0)], nodes[target])
print(sum(nodes[x] for x in s) - nodes[(0,0)])


