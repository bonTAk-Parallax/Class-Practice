class subsets:
    tlst=[4, 5, 6, 7, 8]
    def operation(self):
        lst = self.tlst
        result = []
        result.append([])
        n = len(lst)
        i = 0
        while i<n:
            result.append([lst[i]])
            j = 0
            while j<n:
                if lst[i]!=lst[j]:
                    result.append([lst[i],lst[j]])
                j += 1
            i += 1
        result.append(lst)
        print(result)


ob = subsets()
ob.operation()