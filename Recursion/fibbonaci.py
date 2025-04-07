def fibbonaci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbonaci(n - 1) + fibbonaci(n - 2)
    
# Test cases
def test_fibbonaci():
    assert fibbonaci(0) == 0, "Test case 0 failed"
    assert fibbonaci(1) == 1, "Test case 1 failed"
    assert fibbonaci(2) == 1, "Test case 2 failed"
    assert fibbonaci(3) == 2, "Test case 3 failed"
    assert fibbonaci(4) == 3, "Test case 4 failed"
    assert fibbonaci(5) == 5, "Test case 5 failed"
    print("All test cases passed!")

# Run the test cases
if __name__ == "__main__":
    test_fibbonaci()
    # Example usage
    n = 5
    print(f"The {n}th Fibonacci number is {fibbonaci(n)}")