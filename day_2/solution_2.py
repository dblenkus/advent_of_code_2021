horizontal, depth, aim = 0, 0, 0

with open("input.txt") as fh:
    while (line := fh.readline()) != "":
        command, number = line.strip().split(" ")
        number = int(number)

        if command == "forward":
            horizontal += number
            depth += number * aim
        elif command == "down":
            aim += number
        elif command == "up":
            aim -= number

print(horizontal * depth)
