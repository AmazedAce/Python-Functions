# # -*- coding: utf-8 -*-
# """
# Created on Mon Jun  3 13:26:15 2024

# @author: Loren
# """

# # Task 1


# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Error! Division by zero."
#     return a / b

# # Task 2
    
# def get_number(prompt):
#     while True:
#         try:
#             number = float(prompt)
#             return number
#         except ValueError:
#             print("Invalid input. Please enter a number.")

# def get_operation():
#     operations = ['+', '-', '*', '/']
#     while True:
#         operation = input("Enter an operation (+, -, *, /): ")
#         if operation in operations:
#             return operation
#         else:
#             print("Invalid operation. Please enter one of +, -, *, /.")

# def main():
#     print("Welcome to the Calculator App!")
#     while True:
#         num1 = get_number(input("Enter the first number: "))
#         num2 = get_number(input("Enter the second number: "))
#         operation = get_operation()

#         if operation == '+':
#             result = add(num1, num2)
#         elif operation == '-':
#             result = subtract(num1, num2)
#         elif operation == '*':
#             result = multiply(num1, num2)
#         elif operation == '/':
#             result = divide(num1, num2)

#         print(f"The result is: {result}")

#         another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
#         if another_calculation != 'yes':
#             print("Thank you for using the Calculator App!")
#             break

# if __name__ == "__main__":
#     main()


# 2. The Shopping List Maker

# def main():
#     shopping_list = []
#     print("Welcome to the Shopping List Maker!")

#     while True:
#         print("\nOptions:")
#         print("1. Add an item")
#         print("2. Remove an item")
#         print("3. View the list")
#         print("4. Exit")

#         choice = input("Enter your choice (1/2/3/4): ")

#         if choice == '1':
#             add_item(shopping_list)
#         elif choice == '2':
#             remove_item(shopping_list)
#         elif choice == '3':
#             print_list(shopping_list)
#         elif choice == '4':
#             print("Thank you for using the Shopping List Maker! Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please enter 1, 2, 3, or 4.")

# if __name__ == "__main__":
#     main()


# The Grade Analyzer



# def main():
#     grades = []
#     print("Welcome to the Grade Analyzer!")

#     while True:
#         print("\nOptions:")
#         print("1. Add a grade")
#         print("2. Calculate average grade")
#         print("3. Find highest and lowest grade")
#         print("4. Categorize grades into letter grades")
#         print("5. Exit")

#         choice = input("Enter your choice (1/2/3/4/5): ")

#         if choice == '1':
#             grade = float(input("Enter the grade: "))
#             grades.append(grade)
#             print(f"Grade {grade} has been added.")
#         elif choice == '2':
#             average = calculate_average(grades)
#             print(f"The average grade is: {average}")
#         elif choice == '3':
#             highest, lowest = find_highest_and_lowest(grades)
#             print(f"The highest grade is: {highest}")
#             print(f"The lowest grade is: {lowest}")
#         elif choice == '4':
#             letter_grades = categorize_grades(grades)
#             print("Letter grades:")
#             for idx, letter in enumerate(letter_grades, 1):
#                 print(f"Grade {grades[idx-1]} is a {letter}")
#         elif choice == '5':
#             print("Thank you for using the Grade Analyzer! Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

# if __name__ == "__main__":
#     main()


# 4. The Quiz Game

# Task 1: 
    
# questions = [
#     "What is the capital of France?",
#     "What is the largest planet in our solar system?",
#     "Who wrote 'To Kill a Mockingbird'?",
#     "What is the chemical symbol for water?",
#     "How many continents are there on Earth?"
# ]

# answers = [
#     "Paris",
#     "Jupiter",
#     "Harper Lee",
#     "H2O",
#     "7"
# ]

# # Task 2: 
    
# def quiz_user(questions, answers):
#     user_answers = []
#     for question in questions:
#         user_answer = input(question + " ")
#         user_answers.append(user_answer)
#     return user_answers

# # Task 3: 
    


# def score_quiz(questions, answers, user_answers):
#     score = 0
#     for correct_answer, user_answer in zip(answers, user_answers):
#         if correct_answer.lower() == user_answer.lower():
#             score += 1
#     return score

# def main():
#     print("Welcome to the Quiz Game!")
#     user_answers = quiz_user(questions, answers)
#     score = score_quiz(questions, answers, user_answers)
#     print(f"\nYou scored {score} out of {len(questions)}.")

# if __name__ == "__main__":
#     main()



# 5. The Fitness Tracker

# def log_activity():
#     activities = []
#     durations = []
    
#     while True:
#         activity = input("Enter the fitness activity (or 'done' to finish): ")
#         if activity.lower() == 'done':
#             break
#         duration = float(input(f"Enter the duration in minutes for {activity}: "))
#         activities.append(activity)
#         durations.append(duration)
    
#     return activities, durations


# # Task 2

# def calculate_calories_burned(durations):
#     total_calories = sum(duration * 3.5 for duration in durations)
#     return total_calories

# # Task 3

# def summarize_activities(activities, durations):
#     print("\nActivity Summary:")
#     for activity, duration in zip(activities, durations):
#         print(f"{activity}: {duration} minutes")
#     total_calories = calculate_calories_burned(durations)
#     print(f"\nTotal calories burned: {total_calories:.2f}")

# def main():
#     print("Welcome to the Fitness Tracker!")
#     activities, durations = log_activity()
#     summarize_activities(activities, durations)

# if __name__ == "__main__":
#     main()

