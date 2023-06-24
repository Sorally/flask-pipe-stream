import random
import sys
import time


while True:
    data = sys.stdin.buffer.read(1)
    if not data:
        break
    data = data.decode().upper()
    time.sleep(0.5)
    print(data, end='')
    sys.stdout.flush()
    r = random.randint(1, 100)
    if (r < 5):
        print(f'p2: r is {r}!', file=sys.stderr)
        print('p2 is packing up and leaving, bye!', file=sys.stderr)
        exit(99)


with open("p2.txt", "w") as f:
    f.write("done!!\n")

