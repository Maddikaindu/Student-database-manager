#Desigining  and building a commnad line application that manages student records.
import sqlite3
import csv
import os
with sqlite3.connect("students.db") as students_info:
    cursor=students_info.cursor()
    cursor.execute("Drop table if exists students")
    cursor.execute("""create table students(
            id integer primary key autoincrement ,
            name text not null,
            age integer ,
            grade text
            ); """)
    cursor.execute(""" insert into students(id,name,age,grade)
    values('1','Bob','15','A')""")
    cursor.execute(""" insert into students(id,name,age,grade)
    values('2','Alice','14','B')""")
    cursor.execute("""insert into students(id,name,age,grade)
    values('3','Charlie','13','C')""")
    students_info.commit()
def add_student():
    print("To add more students to the database")
    with sqlite3.connect("students.db") as students_info:
        cursor=students_info.cursor()
        name=input("Enter the name of student:")
        age=input("Enter the age of student:")
        grade=input("Enter the grade of student:")
        cursor.execute("insert into students(name,age,grade) values(?,?,?)",(name,age,grade))
        students_info.commit()
        print("Student added successfully!")
def view_students():
    with sqlite3.connect("students.db") as students_info:
        cursor=students_info.cursor()
        cursor.execute("select * from  students")
        rows=cursor.fetchall()
        for row in rows:
            print({
                "Id" : row[0],
                "Name" : row[1],
                "Age" : row[2],
                "grade" : row[3]
                })
def view_students_sorted():
    with sqlite3.connect("students.db") as students_info:
        cursor=students_info.cursor()
        cursor.execute("select * from  students order by name Asc")
        for row in cursor.fetchall():
            print({
                "Id" : row[0],
                "Name" : row[1],
                "Age" : row[2],
                "grade" : row[3]
                })

def delete_student():
    with sqlite3.connect("students.db") as students_info:
        cursor = students_info.cursor()
        student_id = input("Enter student id to delete: ")
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        students_info.commit()


def update_student():
    with sqlite3.connect("students.db") as students_info:
        cursor=students_info.cursor()
        student_id=input("Enter student id to update: ")
        name=input("Enter the name of student:")
        age=input("Enter the age of student:")
        grade=input("Enter the grade of student:")
        cursor.execute("Update students Set name = ?,age = ?,grade = ? where id = ?",(name,age,grade,student_id))
        students_info.commit()

def export_to_csv():
    with sqlite3.connect("students.db") as students_info:
         cursor=students_info.cursor()
         cursor.execute("select * from  students")
         rows=cursor.fetchall()
         filename=input("Enter the file name as csv:")
         with open(filename,"w",newline="") as output_csv:
            fieldnames=["id","name","age","grade"]
            writer=csv.DictWriter(output_csv,fieldnames=fieldnames)
            writer.writeheader()
            for row in rows:
                writer.writerow({ 
                    "id": row[0],
                    "name": row[1],
                    "age": row[2],
                    "grade": row[3]
                })
            print(os.path.abspath(filename))

def menu():
    while True:
        print("----Student Data Manager----")
        print("1.Add Student")
        print("2.View All Student")
        print("3.Sorting according to names")
        print("4.Delete Student")
        print("5:Update Student")
        print("6.Export to CSV")
        print("7.Exit")
        choice = input("Enter your choice : ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            view_students_sorted()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            update_student()
        elif choice == '6':
            export_to_csv()
        elif choice == '7':
            print("Exiting")
            break
        else:
            print("Invalid Choice.Tryagain")
if __name__ == "__main__":
    menu()

        
        
            
            
        


        
