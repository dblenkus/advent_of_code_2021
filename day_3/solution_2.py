class Node:
    def __init__(self, rep=""):
        self.zero = None
        self.one = None
        self.rep = rep
        self.count = 0

    def process(self, bits):
        if not bits:
            return

        if bits[0] == "0":
            nxt = self.zero = self.zero or Node("0")
        else:
            nxt = self.one = self.one or Node("1")

        nxt.count += 1
        nxt.process(bits[1:])

    def _get(self, func):
        if not self.zero and not self.one:
            return self.rep

        if self.zero and self.one:
            nxt = self.zero if func(self.zero.count, self.one.count) else self.one
        else:
            nxt = self.zero or self.one

        return self.rep + nxt._get(func)

    def get_most(self):
        return self._get(int.__gt__)

    def get_least(self):
        return self._get(int.__le__)


tree = Node()

with open("input.txt") as fh:
    while (line := fh.readline()) != "":
        tree.process(line.strip())

oxy_rating = int(tree.get_most(), 2)
co2_rating = int(tree.get_least(), 2)

print(oxy_rating * co2_rating)
