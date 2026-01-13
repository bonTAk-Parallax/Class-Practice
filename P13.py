class target:
    tlst = [1, 8, 5, 6, 4, 3, 2, 9]
    def __init__(self, num):
        self.num = num

    def check(self):
        n = self.num
        lst = self.tlst
        i = 0
        while i<len(lst):
            for j in lst:
                if j!=lst[i]:
                    res=lst[i]+j
                    if res == n:
                        print(f"Target {n} met seen due to sum of numbers {lst[i]} and {j}.")
            i += 1

        

ob = target(13)
ob.check()