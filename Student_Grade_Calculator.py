def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent! Outstanding work! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good Job! Keep improving! 😊"
    elif marks >= 60:
        return "D", "You passed! Work a little harder next time. 💪"
    else:
        return "F", "Don't give up! Practice and try again. 📚"


# Get student name
name = input("Enter student name: ")

# Input validation using while loop
while True:
    try:
        marks = int(input("Enter marks (0-100): "))

        if 0 <= marks <= 100:
            break
        else:
            print("Marks must be between 0 and 100.")
    except ValueError:
        print("Please enter a valid number.")

# Calculate grade
grade, message = calculate_grade(marks)

# Display result
print("\n📊 RESULT FOR", name.upper())
print("Marks:", marks, "/100")
print("Grade:", grade)
print("Message:", message)