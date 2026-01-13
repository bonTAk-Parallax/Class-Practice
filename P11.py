class reverse:
    def __init__(self, txt):
        self.txt = txt

    def back(self):
        temp = []
        i = 0
        j = -1
        while i<len(self.txt):
            temp.append(self.txt[j])
            j -= 1
            i += 1
        result = ''.join(temp)
        return result


ob = reverse("Python Practice")
print(ob.back())