class American:
    @staticmethod
    def display():
        print("The person is American.")

class NewYorker(American):
    @staticmethod
    def display():
        print("This guy is a new yorker.")

American.display()
NewYorker.display()