# I am developing a browser application that utilizes a stack data structure to manage 
# the history of opened applications. Each time an application is opened, it is pushed 
# onto the stack. When the back button is pressed, applications are popped from the 
# stack in the reverse order of their opening, providing a sequential navigation 
# experience.

class Stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,item):
        self.stack.append(item)
    