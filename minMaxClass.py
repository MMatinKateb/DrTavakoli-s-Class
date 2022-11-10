class Stats:
    def __init__(self):
        self.numbers = []

    def add_number(self, val):
        self.numbers.append(val)

    def maximum(self):
        return max(self.numbers)

    def minimum(self):
        return min(self.numbers)

    def average(self):
        return sum(self.numbers) / len(self.numbers)

count = int(input("Enter number of numbers: "))
print('----------------------')
s = Stats()

for i in range(count):
    n = float(input("Enter a number: "))
    s.add_number(n)


print('----------------------\nResults:')
print("Max =", s.maximum())
print("Min =", s.minimum())
print("Avg =", s.average())