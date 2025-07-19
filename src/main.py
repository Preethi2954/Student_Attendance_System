mport csv
import os

DATA_FILE = os.path.join("Students.csv")

def add_students():
    while True:
        print("\n Student Management")
        print(" Add Student")
        print(" Update Student")
        print(" Delete Student")
        print(" Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            student_id = input("Enter new Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            
            with open(DATA_FILE, "r") as file:
                reader = list(csv.reader(file))
                for row in reader[1:]:
                    if row[0] == student_id:
                        print(" Student ID already exists!")
                        break
                else:
                    with open(DATA_FILE, "a", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow([student_id, name, ""])
                        print(f" Student '{name}' added.")

        elif choice == '2':
            student_id = input("Enter Student ID to update: ").strip()
            updated = False

            with open(DATA_FILE, "r") as file:
                rows = list(csv.reader(file))
            
            for i in range(1, len(rows)):
                if rows[i][0] == student_id:
                    new_name = input("Enter new name: ").strip()
                    rows[i][1] = new_name
                    updated = True
                    break

            if updated:
                with open(DATA_FILE, "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)
                print(" Student record updated.")
            else:
                print(" Student ID not found.")

        elif choice == '3':
            student_id = input("Enter Student ID to delete: ").strip()
            deleted = False

            with open(DATA_FILE, "r") as file:
                rows = list(csv.reader(file))

            new_rows = [rows[0]]  # Keep header
            for row in rows[1:]:
                if row[0] != student_id:
                    new_rows.append(row)
                else:
                    deleted = True

            if deleted:
                with open(DATA_FILE, "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(new_rows)
                print(" Student deleted.")
            else:
                print(" Student ID not found.")

        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")
            
def menu():
    while True:
        print("Student Attendance System")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. List Students")
        print("4. Generate Report")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            mark_attendance()
        elif choice == '3':
            list_students()
        elif choice == '4':
            generate_report()
        elif choice == '5':
            print("Exiting system...")
            break
        else:
            print("Invalid choice! Please, Try again..")

if __name__ == "__main__":
    menu()
