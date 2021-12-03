with open("input.txt") as fh:
    bit_count = [int(bit) for bit in fh.readline().strip()]
    line_count = 1

    while (line := fh.readline()) != "":
        line_count += 1
        for pos, bit in enumerate(line.strip()):
            bit_count[pos] += int(bit)

    common_bits = ["0" if count < line_count / 2 else "1" for count in bit_count]
    gamma_rate = int("".join(common_bits), 2)
    epsilon_rate = gamma_rate ^ (2 ** len(common_bits) - 1)

print(gamma_rate * epsilon_rate)
