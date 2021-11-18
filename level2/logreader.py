import random
import time

filename = 'crap.log'

lines = []
with open (filename, 'r') as f:
    lines = f.readlines()

while True:
    n = random.randint(0, len(lines)-1)
    print (n,lines[n])
    time.sleep(2)
