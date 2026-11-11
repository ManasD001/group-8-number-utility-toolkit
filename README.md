# Number Utility Toolkit - Group 8

## What this project does

This menu-based program checks numbers and performs common calculations. It accepts whole numbers, shows each result, and saves completed calculations in `number_utility_results.txt` so the results can be reviewed after the program closes.

## Files in this folder

- `main.py` - the complete Python program.
- `number_utility_results.txt` - saved results. The sample lines in this file are examples; each new calculation is added below them.
- `deliverables/Group_8_Number_Utility_Toolkit.pptx` - presentation slides.

## Requirements

Install Python 3 on the computer. The program uses the Python standard library only, so no extra packages or internet connection are needed.

## Start the program

1. Open the `Number_Utility_Toolkit` folder in File Explorer.
2. Open a terminal in this folder. In VS Code, choose **Terminal > New Terminal** and check that the terminal path ends with `Number_Utility_Toolkit`.
3. Run:

   ```text
   python main.py
   ```

   On some Windows computers, use:

   ```text
   py main.py
   ```

4. The menu appears. Type the number beside the tool you want and press Enter.
5. Follow the prompt. When the tool asks for a number, enter a whole number such as `153`, then press Enter.
6. After the result appears, the menu comes back so another tool can be selected. Choose option `12` to exit.

## Menu options

1. **Prime check** - tells whether the entered number is prime. Numbers below 2 are not prime.
2. **Palindrome check** - checks whether the number reads the same forwards and backwards. A negative sign is counted, so `-121` is not treated as a palindrome.
3. **Armstrong check** - checks whether the number equals the sum of its digits raised to the number of digits. For example, `153` is an Armstrong number.
4. **Perfect number check** - checks whether the positive divisors below the number add up to the number. For example, `28` is perfect because `1 + 2 + 4 + 7 + 14 = 28`.
5. **Digit sum, count and reverse** - shows the sum of the digits, how many digits there are, and the number with its digits reversed. A minus sign is kept on the reversed value.
6. **Fibonacci series** - asks how many values to show, from 0 to 20. The first values are `0, 1, 1, 2, 3, 5`.
7. **Factorial** - calculates the factorial for a value from 0 to 20. For example, `5!` is `5 × 4 × 3 × 2 × 1 = 120`.
8. **GCD and LCM** - asks for two whole numbers and returns their greatest common divisor and least common multiple.
9. **List primes up to N** - lists prime numbers from 2 up to the entered limit. The allowed limit is 2 to 500.
10. **Multiplication tables up to N** - prints tables from 1 through the entered number. The allowed number is 1 to 12.
11. **Show recent results** - displays up to the five most recent saved calculations.
12. **Exit** - closes the program.

## Example session

```text
Choose an option (1-12): 3
Enter a number: 153
Armstrong Check: True
```

The result is also added to `number_utility_results.txt`. Choose option `11` to see saved results from earlier runs.

## Input and error handling

- Menu choices and number prompts accept whole numbers, including negative values when the selected calculation allows them.
- If letters, a blank answer, or a decimal number are entered, the program explains that a whole number is needed and asks again.
- Values outside a tool's allowed range, such as `25` for factorial, show a message and return to the menu.
- If the results file has not been created yet, the program starts with an empty history and creates the file when the first calculation is saved.

## Run the doctest examples

The examples in the function docstrings can be checked from this folder with:

```text
python -m doctest -v main.py
```

The doctest command checks the examples without starting the menu. It may read the results file to confirm that saved history can be loaded.

## Notes about calculations

The factorial and Fibonacci tools use recursive functions because recursion is a required course topic. Their input range is capped so that the program stays responsive. The prime-list and multiplication-table tools use nested loops, as required by the project brief.

## Group members

- Rajesh Chaurasiya
- Manas Dubey
- Sweta
- Pavan Kumar
