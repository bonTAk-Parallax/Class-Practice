#Complete
class operate:
    tlst =  [-25, -10, -7, -3, 2, 4, 8, 10]
    def op(self):
        lst = self.tlst.copy()
        i = 0
        tdct = dict()
        tlst = []
        while i<len(lst):
            print(f"working on: {lst[i]}")
            j = 0
            while j<len(lst)-1:
                temp = self.tlst[:]
                temp.remove(lst[i])
                print(f"Removing {lst[i]}, lst: {temp}")
                print(f"working on j: {temp[j]}")
                current = temp[j]
                sum = lst[i]+temp[j]
                temp.remove(temp[j])
                print(f"lst: {temp}")
                k = 0
                while k<len(temp):
                    print(f"working on k: {temp[k]}")
                    if sum + temp[k] == 0:
                        tlst.append(current)
                        tlst.append(temp[k])
                        tdct.update({lst[i]:tlst})
                        print(f"one zero from i={lst[i]}, j={current}, k={temp[k]}")
                        tlst = []
                    k += 1
                print()
                j += 1
            i += 1

        print(f"Final numbers whose sum = 0:")
        for k,v in tdct.items():
            result = [k, v[0], v[1]]
            print(result)
ob = operate()
ob.op()