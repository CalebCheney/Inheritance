class Person:
    def __init__(self, name, address, telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone

    def print_person(self):
        print(self.__name)
        print(self.__address)
        print(self.__telephone)
    
    

class Customer(Person):
    def __init__(self, name, address, telephone, cust_num, mail):
        Person.__init__(self, name, address, telephone)

        self.__cust_num = cust_num
        self.__mail = mail

    def print_person(self):
        print(self.__name)
        print(self.__address)
        print(self.__telephone)
        print(self.__cust_num)
        print(self.__mail)
        
