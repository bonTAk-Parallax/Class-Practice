class word_reverse:
    def __init__(self, txt):
        self.txt = txt

    def reverse_all(self):
        temp = []
        lst = []
        i = 0
        j = -1
        n = len(self.txt)
        # print(n)
        # print(self.txt[-n])
        while i<n:
            if self.txt[j]!=' ':
                # print(self.txt[j])
                temp.append(self.txt[j])
                if j == -n:
                    lst.append(" ".join(temp))
            elif self.txt[j]==' ':
                # item = " ".join(temp)
                lst.append(" ".join(temp))
                temp = []            
            i += 1
            j -= 1
        
        return lst

    def reverse_each(self):
        use = []
        temp = []
        tlst = self.reverse_all()
        # print(tlst)
        for lst in tlst:
            # print(lst)
            i = 0
            j = -1
            while i<len(lst):
                temp.append(lst[j])
                i+=1
                j-=1
            temp.append(" ")
            use.append(''.join(temp))
            temp = []
        return " ".join(use)

                
ob = word_reverse("Hello world, how are you doing?")
print("")
print(f"{ob.reverse_each()}")