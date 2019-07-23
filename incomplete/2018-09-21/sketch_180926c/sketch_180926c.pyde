import itertools as it
import random

def setup():
    size(510, 1000)
    frameRate(2)
    
def draw():
    
    all_routes = ['{0:015b}'.format(x) for x in range(2 ** 15)]
    all_routes_lengthisok = [x.count('1') == 10 for x in all_routes]
    correct_routes = list(it.compress(all_routes, all_routes_lengthisok))
    
    input1 = ''.join(correct_routes[random.randint(0,3003)])
    input_list = [int(x) for x in list(input1)]
    
    background(200, 200, 200)
    
    strokeWeight(1)
    stroke(255)
    
    for x in range(6):
        for y in range(11):
            line(100 * x, 0, 100 * x, 1000)
            line(0, 100 * y, 500, 100 * y)

    stroke(255, 0, 0)
    strokeWeight(4)
    
    x = 0
    y = 0
    size = 100
    
    for i in range(len(input_list)):
        if not input_list[i]:
            line(x, y, x + size, y)
            x += size
        else:
            line(x, y, x, y + size)
            y += size
