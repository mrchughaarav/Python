class Book:
    def __init__ (self, authour, setting_title, is_borrowed):
        self.authour = authour
        self.setting_title = setting_title
        self.is_borrowed = is_borrowed
        is_borrowed = False
    def borrow():
        is_borrowed = True
        print("The book has been borrowed.")
    def return_book():
        is_borrowed =  False
        print("The book has been returned.")

b = Book()
b.borrow()
Harry_potter = Book("J.K Rowling", "Harry Potter", True)
Diary_of_a_wimpy_kid = Book("Jeff Kinney","Diary of a wimpy kid", True )
Diary_of_a_wimpy_kid_dogdays = ("Jeff Kinney","Dog days", True)
b.return_book