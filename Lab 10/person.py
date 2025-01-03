class Person():
    #assign values
    def __init__(self, first_name="", last_name="", address="", city="", zip=""):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.zip = zip

    #creating accessor and mutator methods
    def getfn(self):
        return self.first_name

    def getln(self):
        return self.last_name

    def getaddr(self):
        return self.address

    def getcity(self):
        return self.city

    def getzip(self):
        return self.zip

    def setfn(self, first_name):
        self.first_name = first_name

    def setln(self, last_name):
        self.last_name = last.name

    def setaddr(self, address):
        self.address = address

    def setcity(self, city):
        self.city = city

    def setzip(self, zip):
        self.zip = zip

    #full name method
    def get_full_name(self):
        return print('Name: {} {}'.format(self.getfn(), self.getln()))

    #address method
    def get_full_address(self):
        return print('Address: {}, {}, {}'.format(self.getaddr(), self.getcity(), self.getzip()))

    #greetings method
    def greeting(self):
        return print('Welcome {} {}'.format(self.getfn(), self.getln()))

    
