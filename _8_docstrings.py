# Implement a function or class to represent docstring

# In Python, a docstring is a string literal that is used to document a module, class, function, or method. Docstrings are a way to provide a brief description of what the code does, as well as any relevant information about its usage, parameters, return values, and other important details. They are typically placed at the beginning of the code block, immediately after the definition line.

class Square:
    '''
    This is a Square class and have square method
    '''
    
    def square(self,n):
        """
        Returns the square of a given number.

        Args:
            number (int or float): The number to be squared.

        Returns:
            int or float: The square of the input number.
        """
        return n ** 2
    
sq = Square()

# docstring of class
print(Square.__doc__)

# docstring of square method
print(sq.square.__doc__)

print(sq.square(3))