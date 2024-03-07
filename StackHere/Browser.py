# I am developing a browser application that utilizes a stack data structure to manage
# the history of opened applications. Each time an application is opened, it is pushed
# onto the stack. When the back button is pressed, applications are popped from the
# stack in the reverse order of their opening, providing a sequential navigation
# experience.


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


# Initialize an empty stack
stack = Stack()


# Function to add an application to the stack
def open_application(app_name):
    stack.push(app_name)
    print(f"{app_name} opened. Stack: {stack.stack}")


# Function to remove an application from the stack
def go_back():
    app_name = stack.pop()
    if app_name:
        print(f"{app_name} closed. Stack: {stack.stack}")
    else:
        print("Stack is empty.")


open_application("App1")
open_application("App2")
open_application("App3")

go_back()  # Removes "App3" from the stack
go_back()  # Removes "App2" from the stack
go_back()  # Removes "App1" from the stack
go_back()  # Stack is empty
