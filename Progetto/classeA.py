from Progetto.subproject.SubClassA import SubClassA
from Progetto.ClasseB import ClassB

class ClassA:
    def __init__(self):
        self.sba = SubClassA()
        self.clb = ClassB()

    def printClassName(self):
        print('Class A and ')
        self.sba.printClassName()
        self.clb.printClassName()


# if __name__ == '__main__':
#     cl = ClassA()
#     cl.printClassName()

def stampa():
    cl = ClassA()
    cl.printClassName()







