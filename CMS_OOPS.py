# BLL
import pickle
class Customer:
    cuslist = []

    def __init__(self):
        self.id = 0
        self.age = 0
        self.name = 0

    def addCostumer(self):
        Customer.cuslist.append(self)

    def searchCostumer(self):
        for e in Customer.cuslist:
            if e.id == self.id:
                self.age = e.age
                self.name = e.name
                return True
        else:
            return False

    def deleteCostumer(self):
        a = Customer()
        for e in Customer.cuslist:
            if e.id == self.id:
                a = e
                break;
        Customer.cuslist.remove(a)

    def modifyCostumer(self):
        for e in Customer.cuslist:
            if e.id == self.id:
                e.age = self.age
                e.name = self.name
                break



    @staticmethod
    def savetoPickle():
        f = open("C://Users//Adarsh//Desktop//mypickle.txt", "wb")
        pickle.dump(Customer.cuslist, f)
        f.close()

    @staticmethod
    def loadfromPickle():
        f = open("C://Users//Adarsh//Desktop//mypickle.txt", "rb")
        Customer.cuslist = pickle.load(f)
        f.close()

# PL
if __name__ == "__main__":

    def displayCostumer(self):
        print("Costumer id \t Costumer Age \t Costumer Name")
        for e in Customer.cuslist:
            print(e.id, e.age, e.name, sep="\t\t\t\t")


    while (1):
        print("Press 1 to Add Costumer\n"
              "Press 2 to Search Costumer\n"
              "Press 3 for Deleting a Costumer\n"
              "Press 4 to Modify a costumer\n"
              "Press 5 to Display All\n"
              "Press 6 to Exit")
        ch = int(input("Enter Choice:"))
        if ch == 1:
            cus = Customer()
            cus.id = input("Enter Id:")
            cus.age = int(input("Enter age:"))
            cus.name = input("Enter Name:")
            cus.addCostumer()
            print("Addition Successful")
        elif ch == 2:
            cus = Customer()
            cus.id = input("Enter Id:")
            cus.searchCostumer()
        elif ch == 3:
            cus = Customer()
            cus.id = input("Enter Id:")
            cus.deleteCostumer()
            print("Deleted Successfully")
        elif ch == 4:
            cus = Customer()
            cus.id = input("Enter Id:")
            cus.age = int(input("Enter new age:"))
            cus.name = input("Enter new Name:")
            cus.modifyCostumer()
        elif ch == 5:
            cus = Customer()
            cus.displayCostumer()
        elif ch == 6:
            print("Thanks mate")
            break
