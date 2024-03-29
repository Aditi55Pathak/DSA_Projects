# double ended queue for a book shelf where you can insert or remove the books from both ends

from collections import deque

class Bookshelf:
    def __init__(self):
        self.bookshelf=deque()
    
    def appendbookleft(self,book):
        self.bookshelf.appendleft(book)

    def appendbookright(self,book):
        self.bookshelf.append(book)

    def removebookleft(self):
        if len(self.bookshelf) > 0:
            self.bookshelf.popleft()
        else:
            return None
        
    def removebookright(self):
        if len(self.bookshelf) > 0:
            self.bookshelf.pop()
        else:
            return None
        
    def displayBook(self):
        print("Total book in self : ")
        for books in self.bookshelf:
            print(books)

# I am creating here a bookself
            
bookshelf=Bookshelf()

# Adding books from left

bookshelf.appendbookleft("Java")
bookshelf.appendbookleft("C++")
bookshelf.appendbookleft("Ruby")

bookshelf.displayBook()

# Adding books from right

bookshelf.appendbookright("Python")
bookshelf.appendbookright("Scipy")
bookshelf.appendbookright("AI")
    
bookshelf.displayBook()

# Removing books from left and right

bookshelf.removebookleft()
bookshelf.removebookright()

bookshelf.displayBook()

