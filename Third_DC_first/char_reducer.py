import sys

current_char = None
count = 0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue  # skip empty lines

    parts = line.split('\t')
    if len(parts) != 2:
        continue  # skip bad lines

    char, value = parts
    value = int(value)

    if char == current_char:
        count += value
    else:
        if current_char:
            print(f"{current_char}\t{count}")
        current_char = char
        count = value

if current_char:
    print(f"{current_char}\t{count}")
