class Sample():
    offprice = 10

    def getPen(self, color):
        print("This Product:  Price Is 3$ (color {})".format(color))
        self.offPrice(3)
        print("Hot Off!! 50% Pen + NoteBook")
        self.offprice = 50
        self.offPrice(6)


    def getNotebook(self, color):
        print("This Product : NoteBook Is 3$ (color {})".format(color))
        self.offPrice(3)
        print("Hot Off!! 50% Pen + NoteBook")
        self.offprice = 50
        self.offPrice(6)


    @classmethod
    def offPrice(cls,number):
            off = (number * cls.offprice) / 100
            price = number - off
            print("Your Price Is {}$".format(price))

    @staticmethod
    def Sum(num1,num2):
        print(num1+num2)
