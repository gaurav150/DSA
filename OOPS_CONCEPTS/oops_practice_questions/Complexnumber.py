class ComplexNumber:
    def __init__(self, real, imaginary):
        # Initialize real and imaginary parts
        self.real = real
        self.imaginary = imaginary
    
    def add(self, other):
        # Add another ComplexNumber object
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
        else:
            raise ValueError("The operand must be a ComplexNumber.")
    
    def subtract(self, other):
        # Subtract another ComplexNumber object
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
        else:
            raise ValueError("The operand must be a ComplexNumber.")
    
    def multiply(self, other):
        # Multiply by another ComplexNumber object
        if isinstance(other, ComplexNumber):
            real_part = (self.real * other.real) - (self.imaginary * other.imaginary)
            imaginary_part = (self.real * other.imaginary) + (self.imaginary * other.real)
            return ComplexNumber(real_part, imaginary_part)
        else:
            raise ValueError("The operand must be a ComplexNumber.")
    
    def __eq__(self, other):
        # Compare two ComplexNumber objects
        if isinstance(other, ComplexNumber):
            return self.real == other.real and self.imaginary == other.imaginary
        return False
    
    def __str__(self):
        # Return string representation of the complex number
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {abs(self.imaginary)}i"

# Example usage
if __name__ == "__main__":
    c1 = ComplexNumber(3, 2)
    c2 = ComplexNumber(1, 7)

    # Addition
    c3 = c1.add(c2)
    print(f"Addition: {c3}")  # Output: 4 + 9i

    # Subtraction
    c4 = c1.subtract(c2)
    print(f"Subtraction: {c4}")  # Output: 2 - 5i

    # Multiplication
    c5 = c1.multiply(c2)
    print(f"Multiplication: {c5}")  # Output: -11 + 23i

    # Equality
    print(c1 == c2)  # Output: False
    c6 = ComplexNumber(3, 2)
    print(c1 == c6)  # Output: True