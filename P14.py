#incomplete
class operate:
    tlst =  [-25, -10, -7, -3, 2, 4, 8, 10]
    def op(self):
        lst = self.tlst
        i = 0
        while i<len(lst)-1:
            print(lst[i])
            i += 1
            j = 0
            while j<len(lst):
                if lst[j]!= lst[i]:
                    print(lst[j])
                j += 1


ob = operate()
ob.op()