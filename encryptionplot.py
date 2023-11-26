import sys
import math
import matplotlib.pyplot as plt
link = []
escape = 2
bamboo = lambda boobs: math.ceil(math.comb(ord(boobs), f))
for char in sys.argv[1]:
    link.append(char)
f = 97
plt.plot(list(map(bamboo, link)))
plt.show()
while escape != 1:
    enc = ""
    for boop in range(len(link) - 1):
        f = ord(link[boop]) - ord(link[boop-1])
        if f < 0 :
            f = f * -1
        f += 97
        enc += chr(f)
    link = []
    for boo in enc:
        link.append(boo) 
    escape = len(link)
    print(''.join(link))
    plt.plot(list(map(bamboo, link)))
    
plt.show()
