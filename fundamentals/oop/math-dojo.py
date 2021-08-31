class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        for n in nums:
            self.result += n
        self.result += num
        return self

    def subtract(self, num, *nums):
        for n in nums:
            self.result -= n
        self.result -= num
        return self



md = MathDojo()
x = md.add(2,5,5,6,7,8).add(5).subtract(9,9).add(50).subtract(5,5,10).subtract(15).result
print(x)

