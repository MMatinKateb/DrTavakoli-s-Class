class Cal:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def f1(self):
        return self.a + self.b

    def f2(self):
        return self.a - self.b

    def f3(self):
        return self.a * self.b

    def f4(self):
        return self.a / self.b

a = float(input('a='))
b = float(input('b='))
c = input('+ * - / = ')

c1 = Cal(a, b)

if c == '+':    print(c1.f1())
elif c == '-':  print(c1.f2())
elif c == '*':  print(c1.f3())
elif c == '/':  print(c1.f4())
else:   print("Your character is wrong")