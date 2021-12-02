horizontal, depth = 0, 0

with open("input.txt") as fh:
    while (line := fh.readline()) != "":
        command, number = line.strip().split(" ")
        number = int(number)

        if command == "forward":
            horizontal += number
        elif command == "down":
            depth += number
        elif command == "up":
            depth -= number

print(horizontal * depth)
