class myClass:
    __privateVar = 27;
    def __privMeth(self):
        print("I am inside my class")
    def hello(self):
        print("Private Varible value : ", myClass.__privateVar)


foo = myClass()
foo.hello()
