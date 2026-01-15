class fib:
    def __init__(self, num):
        self.n = num 
        # print(self.n)

    def operation(self,n, a=0, b=1):
        
        if n == 0:
            return a
        else:
            n -= 1
            print("000000",a)
            return self.operation(n, a = b, b = a+b)
        
ob = fib(10)
ob.operation(10)