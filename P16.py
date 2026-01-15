class Fact:
    def operation(self, n):
        if n==0 or n==1:
            return n
        else:
            return n*self.operation(n-1)

ob = Fact()
print(ob.operation(5))