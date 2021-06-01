import time
import random

with open('joni.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines() if l.strip()]
    l = random.choice(lines)

def accuracy(x, y):
    a = 0
    missed = ''
    if(len(x) != len(y)):
        ma = max(x, y)
        mi = min(x, y)
        mi += ' '*(len(ma)-len(mi))
        x, y = ma, mi
    for i in range(len(x)):
        if(x[i] == y[i]):
            a += 1
    for i in y:
        if(i not in x):
            if(i not in missed):
                missed += i
    return 100*a/len(x), missed
t = time.time()
print(l)
a = input('> ')
acc, missed = accuracy(l, a)
print('Accuracy: ' + str(round(acc, 2)) + '%')
if(missed):
    print('Chars missed:', ', '.join([i for i in missed]))
speed = time.time()-t
print(len(a), 'chars in', round(speed, 2), 'seconds.')
print(round(len(a)/speed, 2), 'chars per second.')

