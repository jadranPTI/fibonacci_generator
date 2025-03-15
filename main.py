from fibonacci_numpy import fibonacci_iterative

if __name__ == "__main__":
    try:
        num = int(input("Enter the Fibonacci sequence index: "))

        if num < 0:
            print("Please enter a non-negative integer.")
        else:
            result = fibonacci_iterative(num)
            print(f"The {num}th Fibonacci number is: {result}")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")
