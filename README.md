Pattern Generator and Number Analyzer

Project Overview

The Pattern Generator and Number Analyzer is a menu-driven Python application developed to demonstrate basic programming concepts such as loops, nested loops, conditional statements, and control statements.

This project allows users to generate a right-angled triangle pattern and analyze a range of numbers by identifying odd and even numbers and calculating their sum.

Features

1. Pattern Generator

Generates a right-angled triangle pattern using asterisks (*).

Accepts the number of rows from the user.

Uses nested for loops to control rows and columns.

Validates user input to ensure the number of rows is positive.

2. Number Analyzer

Accepts starting and ending numbers from the user.

Uses the range() function to generate numbers within the given range.

Identifies whether each number is odd or even.

Calculates and displays the sum of all numbers in the range.

3. Menu-Driven Interface

The program provides three menu options:

Generate a Right-Angled Triangle.

Analyze a Range of Numbers.

Exit the Program.

4. Error Handling and Input Validation

Validates the number of rows.

Checks that the ending number is greater than the starting number.

Displays appropriate error messages for invalid inputs.

Programming Concepts Used

Python Programming

for and while loops

Nested loops

if, elif, and else statements

break and continue statements

pass statement

range() function

User input and type conversion

Input validation

Technologies Used

Programming Language: Python

IDE: VS Code / Python IDLE

How to Run the Project

Clone or download this repository.

Open the project folder in VS Code or Python IDLE.

Open the terminal.

Run the following command:

python pattern_generator.py

Sample Output

Right-Angled Triangle Pattern

*
* *
* * *
* * * *
* * * * *

Number Analysis

Enter the starting number: 1
Enter the ending number: 10

Number Analysis:
1 is Odd
2 is Even
3 is Odd
4 is Even
5 is Odd
6 is Even
7 is Odd
8 is Even
9 is Odd
10 is Even

Sum of all numbers: 55

Project Structure

Pattern-Generator-and-Number-Analyzer/
│
├── pattern_generator.py
└── README.md

Learning Outcomes

Through this project, I learned how to:

Implement nested loops to generate patterns.

Analyze numbers using loops and conditional statements.

Apply control statements in Python.

Validate user input and handle errors.

Develop a menu-driven console application.

Conclusion

This project demonstrates the practical implementation of Python loops, conditional statements, and control structures through pattern generation and number analysis.
