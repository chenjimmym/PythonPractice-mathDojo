class mathDojo(object):
    def __init__(self):
        self.num = 0
    def add(self, *arg):
        for data in arg:
            self.num += data
        return self
    def subtract(self, *arg):
        for data in arg:
            self.num -= data
        return self
    def result(self):
        print self.num
        return self

md = mathDojo()
md.add(2).add(2,5).subtract(3,2).result()