🧠 Python Quiz Management System
📋 Overview:
The Python Quiz Management System is a console-based application that allows users to take quizzes and admins to manage quiz questions efficiently.
It demonstrates fundamental Python programming concepts such as functions, loops, conditional statements, and file handling.

This project is ideal for beginners learning Python or developing their first command-line project.

🎯 Objective
The goal of this project is to create an interactive quiz system with two major roles:
Admin — who manages quiz questions
User — who attempts quizzes and receives scores and feedback
This helps in understanding role-based logic, data persistence, and modular programming in Python.
🧩 Features

👨‍💼 Admin Features
Add new quiz questions
View all existing questions
Update or delete questions
Manage quiz data (store, modify, delete)
Data stored permanently using file handling

👩‍🎓 User Features
Attempt quiz questions
Get immediate feedback after submission
View total score after completing the quiz
Simple and interactive user interface

⚙️ Technologies Used
Component	Description
Language	Python 3
Concepts Used	Functions, Loops, Conditional Statements
Storage	File Handling (text files)
Interface	Command Line Interface (CLI)
🧠 Python Concepts Demonstrated

This project covers essential Python fundamentals:
Functions → for modular code
Conditional Statements (if-elif-else) → for role and answer checking
Loops (for, while) → for menu and quiz question iteration
File Handling → to store and retrieve questions persistently
Data Structures → lists and dictionaries for managing quiz data

🪜 Project Flow
Start the Application
User is asked to choose between Admin or User login.
Admin Login
Access protected by credentials.
Admin can add, edit, delete, or view questions.
User Login
Users can start a quiz.
Questions are loaded from the file.
After completing the quiz, total score and performance are displayed.
Exit Program

🧰 How to Run the Project
Step 1: Clone the repository
git clone https://github.com/yourusername/python-quiz-system.git

Step 2: Navigate to the project directory
cd python-quiz-system

Step 3: Run the Python file
python quiz.py

Step 4: Follow the on-screen instructions

Choose whether to log in as Admin or User and continue accordingly.

📂 File Structure
📦 python-quiz-system
 ┣ 📜 quiz.py
 ┣ 📜 questions.txt
 ┣ 📜 README.md


quiz.py → main logic of the application
questions.txt → stores quiz questions and answers
README.md → project documentation

🧮 Sample Output
--------------------------------
 Welcome to Python Quiz System
--------------------------------
1. Admin Login
2. User Login
3. Exit
Enter your choice: 2

Question 1: What is the output of 2**3?
a) 6
b) 8
c) 9
d) 12
Your answer: b

Question 2: Which keyword is used to define a function in Python?
a) def
b) function
c) lambda
d) define
Your answer: a

✅ Quiz Completed!
Your Total Score: 2 / 2
Excellent work!

💡 Future Enhancements

Integrate MySQL or SQLite database for better data storage
Add a login system for multiple users
Create a Graphical User Interface (GUI) using Tkinter or Django
Add timer functionality for each question
Implement multiple quiz categories (Python, SQL, Aptitude, etc.
