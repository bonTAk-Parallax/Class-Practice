class power:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def operation(self):
        temp = 1
        for i in range(1, self.n+1):
            temp = temp*self.x
        return temp
    
ob = power(2, 4)
print(ob.operation())