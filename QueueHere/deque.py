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
        if len(self.bookshelf)>0:
            self.bookshelf.popleft()
        else:
            return None
        
    def removebookright(self):
        pass