with open("input.txt") as fh:
    next_depth = int(fh.readline().strip())

    count = 0
    while (depth := fh.readline().strip()) != "":
        current_depth = next_depth
        next_depth = int(depth)

        if next_depth > current_depth:
            count += 1

print(count)
