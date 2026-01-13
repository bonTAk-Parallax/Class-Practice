
class check:
    def __init__(self, txt):
        self.txt = txt

    # def valid(self):
    #     tlst = [['(', ')'], ['{', '}'], ['[', ']']]
    #     temp = []
    #     i = 0
    #     while i<len(tlst):
    #         lst = [x for x in tlst]
    #         j = 0
    #         while j<len(lst)-1:
    #             k = 0
    #             while k<len(self.txt):
    #                 if self.txt[k] == tlst[i][j]:
    #                     print(tlst[i][j])
    #                     temp.append(tlst[i][j])
    #                 k += 1
    #                 print(temp)
    #                 # if len(temp)>2:
    #                 #     val = temp.pop(-2)
    #                 #     try:
    #                 #         if val != tlst[i][j+1]:
    #                 #             print(val)
    #                 #     except:
    #                 #         raise ValueError("Incorrect Paranthesis order")
    #             j += 1
            # i += 1 

    def valid(self):
            str1 = self.txt
            stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
            for parenthese in str1:
                if parenthese in pchar:
                    stack.append(parenthese)
                elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                    return False
            return len(stack) == 0

ck = check("Hello world, (hows) (it) going?")
# ck = check("()[{)}")
print(ck.valid())


        