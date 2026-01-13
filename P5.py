class prac:
    def __init__(self, n):
        self.n = n
        print(self.n)

    def display(self):
        i = 0
        while i<self.n:
            if i%7==0:
                yield i 
            i+=1

ob = prac(50)
# ob.display()
for i in ob.display():
    print(i)
