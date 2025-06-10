from datetime import datetime
class Book:

    def create_library(self,title,author):
        self.title = title
        self.author = author
        self.is_available = True

    def issue(self):
        if self.is_available==False:
            raise Exception ("Not Available")
        
        else:
            print("Book Issued")
            self.is_available == True

    def return_book(self):
        self.is_available == True

        print(f"{self.title} is Available at {datetime.now()}")

    
    def status(self):
        print(f"{self.title} status is {self.is_available} at {datetime.now()}")


book_instance1 = Book()

book_instance1.create_library("Atomic Habbits","James")

book_instance1.issue()

book_instance1.return_book()

book_instance1.status()

    
