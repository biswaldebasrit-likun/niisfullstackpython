# Parent class
class Parent:
    def __init__(self, parent_name):
        self.parent_name = parent_name

    def show_parent(self):
        print("Parent Name:", self.parent_name)


# Child class inheriting from Parent
class Child(Parent):
    def __init__(self, parent_name, child_name):
        super().__init__(parent_name)
        self.child_name = child_name

    def show_child(self):
        print("Child Name:", self.child_name)


# Engineering class inheriting from Child
class Engineering(Child):
    def __init__(self, parent_name, child_name, branch):
        super().__init__(parent_name, child_name)
        self.branch = branch

    def show_engineering(self):
        print("Engineering Branch:", self.branch)


# Creating object
student = Engineering("Ramesh", "Suresh", "Computer Science")

# Accessing methods from all classes
student.show_parent()
student.show_child()
student.show_engineering()