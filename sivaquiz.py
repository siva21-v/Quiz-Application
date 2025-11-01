import mysql.connector
from datetime import datetime
import sys


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Siva@2003",   
    database="quiz_system"
)

admin_id = "admin"
admin_password = "1234"


def add_technology():
    cur = db.cursor()
    tech_name = input("Enter technology name: ").strip().lower()  # convert to lowercase

    
    cur.execute("SELECT * FROM technologies WHERE name = %s", (tech_name,))
    result = cur.fetchone()

    if result:
        print("Technology already exists.")
    else:
        cur.execute("INSERT INTO technologies (name) VALUES (%s)", (tech_name,))
        db.commit()
        print("Technology added successfully.")


def add_question():
    cur = db.cursor()
    cur.execute("SELECT * FROM technologies")
    techs = cur.fetchall()
    if not techs:
        print("No technology found. Add one first.")
        return
    print("Technologies:")
    for t in techs:
        print(f"{t[0]} - {t[1]}")

    tech_id = int(input("Enter technology id: "))
    q = input("Enter question: ")
    a = input("Option A: ")
    b = input("Option B: ")
    c = input("Option C: ")
    d = input("Option D: ")
    ans = input("Correct answer (A/B/C/D): ").upper()

    ans_map = {"A":1,"B":2,"C":3,"D":4}
    ans_num = ans_map.get(ans, 0)

    cur.execute(
        "INSERT INTO questions (technology_id, question, option1, option2, option3, option4, answer) VALUES (%s,%s,%s,%s,%s,%s,%s)",
        (tech_id, q, a, b, c, d, ans_num)
    )
    db.commit()
    print("Question added successfully.")
def modify_question():
    cur = db.cursor()

    
    cur.execute("SELECT * FROM technologies")
    techs = cur.fetchall()
    if not techs:
        print("No technologies found.")
        return

    print("\nAvailable Technologies:")
    for t in techs:
        print(f"{t[0]} - {t[1]}")

    tech_id = int(input("Enter technology ID to select: "))

   
    cur.execute("SELECT * FROM questions WHERE technology_id=%s", (tech_id,))
    questions = cur.fetchall()
    if not questions:
        print("No questions found for this technology.")
        return

    print("\nQuestions for selected technology:")
    for q in questions:
        print(f"ID: {q[0]} | Q: {q[2]}")  

    qid = int(input("Enter question ID to modify: "))

    new_q = input("New question: ")
    new_a = input("Option A: ")
    new_b = input("Option B: ")
    new_c = input("Option C: ")
    new_d = input("Option D: ")
    new_ans = input("Correct option (A/B/C/D): ").upper()

    ans_map = {"A":1, "B":2, "C":3, "D":4}
    ans_num = ans_map.get(new_ans, 0)

    cur.execute(
        "UPDATE questions SET question=%s, option1=%s, option2=%s, option3=%s, option4=%s, answer=%s WHERE id=%s",
        (new_q, new_a, new_b, new_c, new_d, ans_num, qid)
    )
    db.commit()
    print("Question updated successfully.")


def delete_question():
    cur = db.cursor()
    view_questions()  
    qid = int(input("Enter question ID to delete: "))
    cur.execute("DELETE FROM questions WHERE id=%s", (qid,))
    db.commit()
    print("Question deleted.")


def view_questions():
    cur = db.cursor()

    
    cur.execute("SELECT * FROM technologies")
    techs = cur.fetchall()
    if not techs:
        print("No technology found.")
        return

    print("\nAvailable Technologies:")
    for t in techs:
        print(f"{t[0]} - {t[1]}")

    
    tech_name = input("Enter technology name to view questions: ").strip().lower()

    
    cur.execute("SELECT id FROM technologies WHERE LOWER(name)=%s", (tech_name,))
    row = cur.fetchone()
    if not row:
        print("Invalid technology.")
        return
    tech_id = row[0]

   
    cur.execute(
        "SELECT id, question, option1, option2, option3, option4, answer FROM questions WHERE technology_id=%s",
        (tech_id,)
    )
    questions = cur.fetchall()

    if not questions:
        print("No questions found for this technology.")
        return

    print(f"\n--- Questions for {tech_name.title()} ---")
    ans_map = {1: "A", 2: "B", 3: "C", 4: "D"}
    for q in questions:
        print(f"\nID: {q[0]}")
        print(f"Q: {q[1]}")
        print(f"A: {q[2]}")
        print(f"B: {q[3]}")
        print(f"C: {q[4]}")
        print(f"D: {q[5]}")
        print(f"Answer: {ans_map[q[6]]}")
def view_scores():
    cur = db.cursor()
    cur.execute("""
        SELECT s.id, u.username, u.mobile, t.name AS technology,
               s.score, s.total, s.time
        FROM scores s
        JOIN users u ON s.user_id = u.id
        JOIN technologies t ON s.technology_id = t.id
        ORDER BY s.time ASC
    """)
    rows = cur.fetchall()

    if not rows:
        print("\nNo scores found.")
        return

    print("\n--- Scores and Users ---")
    for r in rows:
        print(f"Score ID: {r[0]}, Username: {r[1]}, Mobile: {r[2]}, "
              f"Technology: {r[3]}, Score: {r[4]}/{r[5]}, Time: {r[6]}")

 
def register_user():
    uname = input("Enter username: ").strip()   
    mobile = input("Enter mobile: ").strip()
    
    cur = db.cursor()
    
    
    cur.execute("SELECT * FROM users WHERE username = %s", (uname,))
    result = cur.fetchone()
    
    if result:
        print("Username already exists.")
    else:
        
        cur.execute("INSERT INTO users (username, mobile) VALUES (%s, %s)", (uname, mobile))
        db.commit()
        print("User registered successfully.")


def login_user():
    uname = input("Enter username: ")
    mobile = input("Enter mobile: ")
    cur = db.cursor()
    cur.execute("SELECT id FROM users WHERE username=%s AND mobile=%s", (uname, mobile))
    row = cur.fetchone()
    if row:
        print("Login successful.")
        return row[0]
    else:
        print("Invalid login.")
        return None

from datetime import datetime

def take_quiz(user_id):
    cur = db.cursor()

   
    cur.execute("SELECT * FROM technologies")
    techs = cur.fetchall()
    if not techs:
        print("No technology found.")
        return

    print("\nAvailable Technologies:")
    for t in techs:
        print(f"{t[0]} - {t[1]}")
    tech_name = input("Enter technology name: ").strip().lower()
    cur.execute("SELECT id FROM technologies WHERE LOWER(name) = %s", (tech_name,))
    row = cur.fetchone()
    if not row:
        print("Invalid technology.")
        return
    tech_id = row[0]

 
    cur.execute("SELECT id, question, option1, option2, option3, option4, answer FROM questions WHERE technology_id = %s", (tech_id,))
    questions = cur.fetchall()
    if not questions:
        print("No questions available for this technology.")
        return

    score = 0
    total = len(questions)
    ans_map = {1: "A", 2: "B", 3: "C", 4: "D"} 

    for q in questions:
        print("\nQ:", q[1])
        options = q[2:6]  
        for label, option in zip(["A", "B", "C", "D"], options):
            print(f"{label}: {option}")

        ans = input("Your answer (A/B/C/D): ").upper()
        if ans_map.get(q[6]) == ans: 
            score += 1

    print(f"\nQuiz finished! Your score: {score}/{total}")

   
    cur.execute(
        "INSERT INTO scores (user_id, technology_id, score, total, time) VALUES (%s,%s,%s,%s,%s)",
        (user_id, tech_id, score, total, datetime.now())
    )
    db.commit()



def view_top_scores():
    cur = db.cursor()
    cur.execute("""
        SELECT u.username, u.mobile, s.score, s.total
        FROM scores s
        JOIN users u ON s.user_id = u.id
        ORDER BY s.score DESC, s.time ASC
        LIMIT 3
    """)
    rows = cur.fetchall()
    print("\n--- Top Scores ---")
    for r in rows:
        print(f"User: {r[0]}, Mobile: {r[1]}, Score: {r[2]}/{r[3]}")

 
def admin_menu():
    while True:
        print("\n--- ADMIN MENU ---")
        print("1. Add Technology")
        print("2. Add Question")
        print("3. Modify Question")
        print("4. Delete Question")
        print("5. View All Questions")
        print("6. View Scores and Users")
        print("7. Exit")
        ch = input("Enter choice: ")

        if ch == "1": 
            add_technology()
        elif ch == "2": 
            add_question()
        elif ch == "3": 
            modify_question() 
        elif ch == "4": 
            delete_question()  
        elif ch == "5": 
            view_questions()
        elif ch == "6": 
            view_scores()
        elif ch == "7": 
            break


def user_menu():
    while True:
        print("\n--- USER MENU ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        ch = input("Enter choice: ")
        if ch == "1": register_user()
        elif ch == "2":
            uid = login_user()
            if uid:
                while True:
                    print("\n1. Take Quiz\n2. View Top Scores\n3. Exit")
                    c = input("Enter choice: ")
                    if c == "1": take_quiz(uid)
                    elif c == "2": view_top_scores()
                    elif c == "3": break
        elif ch == "3": break

def main():
    while True:
        print("\n--- QUIZ SYSTEM ---")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            a = input("Admin ID: ")
            p = input("Password: ")
            if a == admin_id and p == admin_password:
                admin_menu()
            else:
                print("Wrong admin login.")
        elif choice == "2":
            user_menu()
        elif choice == "3":
            sys.exit()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

