class mathDojo(object):
    def __init__(self):
        self.num = 0
    def add(self, *arg):
        for data in arg:
            if isinstance(data, list) or isinstance(data, tuple):
                for datas in data:
                    self.num += datas
            else:
                self.num += data
        return self
    def subtract(self, *arg):
        for data in arg:
            if isinstance(data, list) or isinstance(data, tuple):
                for datas in data:
                    self.num -= datas
            else:
                self.num -= data
        return self
    def result(self):
        print self.num
        return self

md = mathDojo()
md.add([1], 3,4).add([3,5,7,8], (2,4.3,1.25)).subtract(2, (2,3), [1.1,2.3]).result()