def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
        fib_sequence.append(b)
    return fib_sequence

def main():
    n = int(input("Enter the number of Fibonacci terms to generate: "))
    fib_sequence = fibonacci_iterative(n)
    print(f"First {n} Fibonacci numbers: {fib_sequence}")

if __name__ == "__main__":
    main()