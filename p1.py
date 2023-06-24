import random
import sys
import time


for i in range(0x61, 0x7b):
    print(chr(i), end='')
    sys.stdout.flush()
    time.sleep(0.5)
    r = random.randint(1, 100)
    if r < 5:
        print(f'p1: r is {r}!', file=sys.stderr)
        print('aborting p1!', file=sys.stderr)
        exit(42)

with open("p1.txt", "w") as f:
    f.write("done!\n")

