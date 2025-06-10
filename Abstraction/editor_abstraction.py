from abc import ABC, abstractmethod

# Abstract base class defining the interface for an Editor
class Editor(ABC):
    
    @abstractmethod
    def open(self):
        """Abstract method to open the editor"""
        pass
    
    @abstractmethod
    def execute(self):
        """Abstract method to execute code in the editor"""
        pass
    
    @abstractmethod
    def debugg(self):
        """Abstract method to debug code in the editor"""
        pass
    
    @abstractmethod
    def edit(self):
        """Abstract method to edit code in the editor"""
        pass

# Concrete implementation of the Editor abstract class
class Pycharm(Editor):
    
    # Implementation of open method
    def open(self):
        """Opens the PyCharm editor"""
        print("Editor Open Method")
    
    # Implementation of execute method
    def execute(self):
        """Executes code in PyCharm"""
        print("Editor Execute Method")
    
    # Implementation of debugg method
    def debugg(self):
        """Debugs code in PyCharm"""
        print("Editor Debugg Method")
    
    # Implementation of edit method
    def edit(self):
        """Edits code in PyCharm"""
        print("Editor Edit Method")

# Create an instance of Pycharm
edit_instance = Pycharm()

# Call each method on the instance
edit_instance.open()      
edit_instance.execute()   
edit_instance.debugg()    
edit_instance.edit()      