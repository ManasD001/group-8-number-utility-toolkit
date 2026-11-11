# Number Utility Toolkit
# Group 8 project for practising basic Python concepts.

import doctest

RESULTS_FILE = "number_utility_results.txt"
MENU = """
NUMBER UTILITY TOOLKIT
1. Check prime
2. Check palindrome
3. Check Armstrong number
4. Check perfect number
5. Digit sum, count and reverse
6. Fibonacci series
7. Factorial
8. GCD and LCM
9. List primes up to N
10. Multiplication tables up to N
11. Show recent results
12. Exit
"""


# Tests divisors only up to the square root.
def is_prime(number):
    """Return True when number is prime.

    >>> is_prime(7)
    True
    >>> is_prime(1)
    False
    """
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


# Compares the digit string with its reverse.
def is_palindrome(number):
    """Check whether the digits read the same both ways.

    >>> is_palindrome(1221)
    True
    >>> is_palindrome(-121)
    False
    """
    digits = str(number)
    return digits == digits[::-1]


# Raises each digit to the number of digits.
def is_armstrong(number):
    """Check whether a non-negative number is an Armstrong number.

    >>> is_armstrong(153)
    True
    >>> is_armstrong(12)
    False
    """
    if number < 0:
        return False
    digits = str(number)
    power = len(digits)
    total = 0
    for digit in digits:
        total += int(digit) ** power
    return total == number


# Adds positive divisors smaller than the number.
def is_perfect(number):
    """Check whether positive proper divisors add up to number.

    >>> is_perfect(28)
    True
    >>> is_perfect(12)
    False
    """
    if number < 2:
        return False
    divisor_sum = 1
    for divisor in range(2, number // 2 + 1):
        if number % divisor == 0:
            divisor_sum += divisor
    return divisor_sum == number


# Calculates three useful facts about a number.
def digit_details(number):
    """Return digit sum, digit count and reversed number as a tuple.

    >>> digit_details(408)
    (12, 3, 804)
    >>> digit_details(-25)
    (7, 2, -52)
    """
    digits = str(abs(number))
    digit_sum = sum(int(digit) for digit in digits)
    reversed_number = int(digits[::-1])
    if number < 0:
        reversed_number = -reversed_number
    return digit_sum, len(digits), reversed_number


# Uses a base case and a smaller recursive call.
def factorial(number):
    """Find factorial by recursion.

    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    if number < 0:
        raise ValueError("Factorial needs a non-negative number.")
    if number <= 1:
        return 1
    return number * factorial(number - 1)


# Finds one Fibonacci value through recursion.
def fibonacci_value(index):
    """Return a Fibonacci value using recursion.

    >>> fibonacci_value(0)
    0
    >>> fibonacci_value(7)
    13
    """
    if index < 0:
        raise ValueError("Index must be non-negative.")
    if index <= 1:
        return index
    return fibonacci_value(index - 1) + fibonacci_value(index - 2)


# Builds a sequence from recursive values.
def fibonacci_series(count):
    """Return the first count Fibonacci values in a tuple.

    >>> fibonacci_series(6)
    (0, 1, 1, 2, 3, 5)
    >>> fibonacci_series(0)
    ()
    """
    return tuple(fibonacci_value(index) for index in range(count))


# Applies the Euclidean algorithm recursively.
def gcd(first, second):
    """Find the greatest common divisor by recursion.

    >>> gcd(24, 18)
    6
    >>> gcd(7, 0)
    7
    """
    first = abs(first)
    second = abs(second)
    if second == 0:
        return first
    return gcd(second, first % second)


# Calculates both common factors for a pair.
def gcd_lcm(first, second):
    """Return GCD and LCM as a fixed tuple.

    >>> gcd_lcm(12, 18)
    (6, 36)
    >>> gcd_lcm(5, 0)
    (5, 0)
    """
    common = gcd(first, second)
    if common == 0:
        return common, 0
    return common, abs(first * second) // common


# Searches candidates with nested loops.
def primes_up_to(limit):
    """Return all primes up to limit as a sorted tuple.

    >>> primes_up_to(10)
    (2, 3, 5, 7)
    >>> primes_up_to(1)
    ()
    """
    prime_set = set()
    for candidate in range(2, limit + 1):
        is_candidate_prime = True
        for divisor in range(2, candidate):
            if candidate % divisor == 0:
                is_candidate_prime = False
                break
        if is_candidate_prime:
            prime_set.add(candidate)
    return tuple(sorted(prime_set))


# Builds tables with an outer and inner loop.
def multiplication_tables(limit):
    """Build tables from 1 to limit as lines of text.

    >>> multiplication_tables(2)
    ('1 x 1 = 1', '1 x 2 = 2', '2 x 1 = 2', '2 x 2 = 4')
    >>> multiplication_tables(0)
    ()
    """
    lines = []
    for number in range(1, limit + 1):
        for multiplier in range(1, limit + 1):
            lines.append(f"{number} x {multiplier} = {number * multiplier}")
    return tuple(lines)


# Cleans a label before displaying or saving it.
def format_result(operation, value):
    """Make a readable line for the result log.

    >>> format_result('prime check', True)
    'Prime Check: True'
    """
    clean_operation = " ".join(operation.strip().lower().split()).title()
    return f"{clean_operation}: {value}"


# Loads earlier result lines when the file exists.
def load_history():
    """Read old result lines; a missing file starts with an empty list.

    >>> isinstance(load_history(), list)
    True
    """
    try:
        with open(RESULTS_FILE, "r", encoding="utf-8") as result_file:
            return [line.strip() for line in result_file if line.strip()]
    except FileNotFoundError:
        return []


# Keeps recent lines and appends the result to disk.
def save_result(line, history):
    """Add one result to the list and append it to the text file.

    >>> callable(save_result)
    True
    """
    history.append(line)
    if len(history) > 100:
        history.remove(history[0])
    with open(RESULTS_FILE, "a", encoding="utf-8") as result_file:
        result_file.write(line + "\n")
    return line


# Selects, sorts and returns the five latest entries.
def show_recent(history):
    """Return the last five saved results, sorted for display.

    >>> show_recent(['c', 'a', 'b'])
    ('a', 'b', 'c')
    """
    recent = history[-5:]
    recent.sort()
    return tuple(recent)


# Repeats the prompt until input is a whole number.
def read_number(prompt):
    """Keep asking until a whole number is entered.

    The menu uses this helper so letters and blank input do not crash it.

    >>> callable(read_number)
    True
    """
    while True:
        answer = input(prompt).strip()
        digits = answer[1:] if answer.startswith("-") else answer
        if digits and digits.isdigit():
            return int(answer)
        print("Please enter a whole number.")


# Runs the menu and calls the selected tool.
def main():
    """Run the menu until the user selects Exit.

    >>> callable(main)
    True
    """
    history = load_history()
    results = {}
    while True:
        print(MENU)
        choice = read_number("Choose an option (1-12): ")
        if choice == 12:
            print("Goodbye!")
            break
        if choice not in range(1, 13):
            print("Choose a number from 1 to 12.")
            continue
        if choice == 11:
            recent = show_recent(history)
            if recent:
                for line in recent:
                    print(line)
            else:
                print("No saved results yet.")
            continue

        try:
            if choice == 1:
                number = read_number("Enter a number: ")
                operation, value = "Prime check", is_prime(number)
            elif choice == 2:
                number = read_number("Enter a number: ")
                operation, value = "Palindrome check", is_palindrome(number)
            elif choice == 3:
                number = read_number("Enter a number: ")
                operation, value = "Armstrong check", is_armstrong(number)
            elif choice == 4:
                number = read_number("Enter a number: ")
                operation, value = "Perfect number check", is_perfect(number)
            elif choice == 5:
                number = read_number("Enter a number: ")
                operation, value = "Digit sum, count, reverse", digit_details(number)
            elif choice == 6:
                count = read_number("How many Fibonacci values (0-20)? ")
                if count < 0 or count > 20:
                    print("Please enter a value from 0 to 20.")
                    continue
                operation, value = "Fibonacci series", fibonacci_series(count)
            elif choice == 7:
                number = read_number("Enter a number (0-20): ")
                if number < 0 or number > 20:
                    print("Please enter a value from 0 to 20.")
                    continue
                operation, value = "Factorial", factorial(number)
            elif choice == 8:
                first = read_number("Enter the first number: ")
                second = read_number("Enter the second number: ")
                operation, value = "GCD and LCM", gcd_lcm(first, second)
            elif choice == 9:
                limit = read_number("List primes up to (2-500): ")
                if not 2 <= limit <= 500:
                    print("Please enter a value from 2 to 500.")
                    continue
                prime_values = primes_up_to(limit)
                results["prime_set"] = set(prime_values)
                operation, value = "Primes up to " + str(limit), prime_values
            elif choice == 10:
                limit = read_number("Print tables up to (1-12): ")
                if not 1 <= limit <= 12:
                    print("Please enter a value from 1 to 12.")
                    continue
                operation, value = "Multiplication tables up to " + str(limit), multiplication_tables(limit)
            else:
                print("Choose a number from 1 to 12.")
                continue
        except (ValueError, OverflowError) as error:
            print("That calculation could not be completed:", error)
            continue

        results[operation] = value
        line = format_result(operation, value)
        print(line)
        save_result(line, history)


if __name__ == "__main__":
    main()











