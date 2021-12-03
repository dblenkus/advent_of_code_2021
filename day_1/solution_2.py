from collections import deque

with open("input.txt") as fh:
    window = deque([int(fh.readline().strip()) for _ in range(3)], maxlen=4)
    next_sum = sum(window)

    count = 0
    while (depth := fh.readline().strip()) != "":
        current_sum = next_sum

        window.append(int(depth))
        next_sum = next_sum - window[0] + window[-1]

        if next_sum > current_sum:
            count += 1

print(count)
