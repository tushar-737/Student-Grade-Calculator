# Student Grade Calculator

## Project Overview

The Student Grade Calculator is a Python program that calculates a student's grade based on marks entered by the user. The program validates the input, assigns a grade according to predefined grading rules, and displays an encouraging message based on the student's performance.

### Objectives

* Learn and apply if-elif-else statements.
* Use functions to create reusable code.
* Implement while loops for input validation.
* Handle invalid user input using error handling.
* Display grades and personalized feedback.

---

## Technical Requirements Met

| Requirement              | Implementation                        |
| ------------------------ | ------------------------------------- |
| if-elif-else statements  | Used for grading logic                |
| Input validation (0-100) | Implemented using while loop          |
| At least one function    | `calculate_grade()` function          |
| Encouraging messages     | Displayed for each grade              |
| While loop               | Repeats until valid marks are entered |
| Error handling           | Uses try-except for invalid inputs    |

---

## Grading Logic

The program assigns grades according to the following scale:

| Marks Range | Grade |
| ----------- | ----- |
| 90 - 100    | A     |
| 80 - 89     | B     |
| 70 - 79     | C     |
| 60 - 69     | D     |
| 0 - 59      | F     |

### Encouraging Messages

* Grade A → "Excellent! Outstanding work!"
* Grade B → "Very Good! Keep it up!"
* Grade C → "Good Job! Keep improving!"
* Grade D → "You passed! Work a little harder next time."
* Grade F → "Don't give up! Practice and try again."

---

## Functions Used

### calculate_grade(marks)

This function accepts the student's marks as input and returns:

1. Grade (A, B, C, D, or F)
2. Encouraging message

Example:

```python
grade, message = calculate_grade(85)
```

Output:

```text
B
Very Good! Keep it up!
```

---

## Code Structure

```text
Student-Grade-Calculator/
│
├── README.md
├── grade_calculator.py
├── test_cases.txt
└── screenshots/
```

### File Descriptions

#### grade_calculator.py

Main program file containing:

* User input
* Input validation
* Grading logic
* Function definition
* Result display

#### test_cases.txt

Contains sample inputs and expected outputs for testing.

#### screenshots/

Contains screenshots showing the program running successfully.

---

## Setup and Installation

### Prerequisites

* Python 3.x installed on your system

### Installation Steps

1. Clone the repository

```bash
git clone https://github.com/tushar-737/Student-Grade-Calculator.git
```

2. Open the project folder

```bash
cd Student-Grade-Calculator
```

3. Run the program

```bash
python grade_calculator.py
```

---

## Sample Output

```text
Enter student name: Priya
Enter marks (0-100): 85

RESULT FOR PRIYA

Marks: 85/100
Grade: B
Message: Very Good! Keep it up!
```

---



## Learning Outcomes

Through this project, I learned:

* Decision making using if-elif-else statements
* Repetition using while loops
* Creating reusable functions
* Input validation techniques
* Basic error handling in Python
* Organizing and documenting Python projects

---

## Author
Tushar Gupta

Tushar Gupta
