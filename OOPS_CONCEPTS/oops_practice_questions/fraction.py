class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()  # Simplify the fraction upon initialization
    
    def _find_gcd(self, a, b):
        """Find the greatest common divisor using the Euclidean algorithm."""
        while b:
            a, b = b, a % b
        return abs(a)
    
    def _simplify(self):
        """Simplify the fraction by dividing the numerator and denominator by their GCD."""
        gcd = self._find_gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        # Ensure the denominator is positive
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator
    
    def add(self, other):
        """Add two fractions."""
        if not isinstance(other, Fraction):
            raise ValueError("The operand must be a Fraction.")
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def subtract(self, other):
        """Subtract two fractions."""
        if not isinstance(other, Fraction):
            raise ValueError("The operand must be a Fraction.")
        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def multiply(self, other):
        """Multiply two fractions."""
        if not isinstance(other, Fraction):
            raise ValueError("The operand must be a Fraction.")
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def divide(self, other):
        """Divide two fractions."""
        if not isinstance(other, Fraction):
            raise ValueError("The operand must be a Fraction.")
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)
    
    def __eq__(self, other):
        """Compare two fractions for equality."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator == other.numerator and self.denominator == other.denominator
    
    def __str__(self):
        """Return string representation of the fraction."""
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self):
        """Return detailed representation of the fraction."""
        return f"Fraction(numerator={self.numerator}, denominator={self.denominator})"

# Example usage
if __name__ == "__main__":
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)

    # Addition
    f3 = f1.add(f2)
    print(f"Addition: {f3}")  # Output: 10/8 or 5/4 after simplification

    # Subtraction
    f4 = f1.subtract(f2)
    print(f"Subtraction: {f4}")  # Output: -1/4

    # Multiplication
    f5 = f1.multiply(f2)
    print(f"Multiplication: {f5}")  # Output: 3/8

    # Division
    f6 = f1.divide(f2)
    print(f"Division: {f6}")  # Output: 2/3

    # Equality
    f7 = Fraction(2, 4)
    print(f1 == f7)  # Output: True