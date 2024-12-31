class Operation:
    def __init__(self, name, number1, number2):
        self.a = number1
        self.number2 = number2
        self.name = name

    def name(self):
        pass

    def symbol(self):
        print('operation')

    def estimate(self):
        pass

class secret(Operation):
    def __init__(self):
        super().__init__(name='secret', number1=1, number2=1)

class add(Operation):
    def __init__(self, number1, number2):
        self.name = "add"
        self.number1 = number1
        self.number2 = number2

    def name(self):
        return self.name

    def symbol(self):
        return "+"

    def estimate(self):
        return self.number1 + self.number2

class mul(Operation):
    def __init__(self, number1, number2):
        self.name = "mul"
        self.number1 = number1
        self.number2 = number2

    def name(self):
        return self.name

    def symbol(self):
        return "*"

    def estimate(self):
        return self.number1 * self.number2

class sub(Operation):
    def __init__(self, number1, number2):
        self.name = "sub"
        self.number1 = number1
        self.number2 = number2

    def name(self):
        return self.name

    def symbol(self):
        return "-"

    def estimate(self):
        return self.number1 - self.number2

class max(Operation):
    def __init__(self, number1, number2):
        self.name = "max"
        self.number1 = number1
        self.number2 = number2

    def name(self):
        return self.name

    def symbol(self):
        return "max"

    def estimate(self):
        max_n = None
        if self.number1 > self.number2:
            max_n = self.number1
        else:
            max_n = self.number2
        return max_n

num1=int(input('Enter the first number: '))
num2=int(input('Enter the second number: '))
print()

Operations = [add, mul, sub, max]

for oprs in Operations:
    obj = oprs(num1, num2)
    print(f'{obj.name}: {num1} {obj.symbol()} {num2} = {obj.estimate()}')

print()
secr = secret()
print(secr)
print(secr.symbol())