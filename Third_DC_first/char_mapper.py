import sys

for line in sys.stdin:
    line = line.strip()
    for ch in line:
        print(f"{ch}\t1")
