class FibonacciIterator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.x, self.y = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        if self.count == 0:
            self.count += 1
            return 0
        elif self.count == 1:
            self.count += 1
            return 1
        else:
            self.x, self.y = self.y, self.x + self.y
            self.count += 1
            return self.y

fibonacci_iterator = FibonacciIterator(10)

for number in fibonacci_iterator:
    print(number)
