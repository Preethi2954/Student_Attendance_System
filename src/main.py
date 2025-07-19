import csv
import os
from datetime import datetime



STUDENT_FILE = "students.csv"
ATTENDANCE_FILE = "attendance.csv"

def mark_attendance():
    if not os.path.exists(STUDENT_FILE):
        print(" Student file not found.")
        return

    date_today = datetime.now().strftime("%Y-%m-%d")
    attendance_records = []

    # Read existing students
    with open(STUDENT_FILE, mode="r", newline="") as sfile:
        reader = csv.reader(sfile)
        student_rows = list(reader)

    if not student_rows or len(student_rows[0]) < 2:
        print(" No valid student records found.")
        return

    # Read existing attendance (if any)
    existing_attendance = []
    if os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, mode="r", newline="") as afile:
            existing_attendance = list(csv.reader(afile))

    # Prepare header
    header = ["ID", "Name", "Attendance", "Date"]
    new_attendance = []

    print("\n Marking Attendance for Today:", date_today)

    for row in student_rows[1:]:  # Skip header
        student_id, name = row[0], row[1]

        # Check if this student's attendance already exists for today
        already_marked = False
        for record in existing_attendance:
            if len(record) == 4 and record[0] == student_id and record[3] == date_today:
                already_marked = True
                print(f"\nStudent: {name} (ID: {student_id}) - Already marked: {record[2]}")
                update = input("Do you want to update it? (y/n): ").strip().lower()
                if update == 'y':
                    status = input("Enter new attendance (P/A): ").strip().upper()
                    if status not in ['P', 'A']:
                        status = ""
                    record[2] = status
                new_attendance.append(record)
                break

        if not already_marked:
            print(f"\nStudent: {name} (ID: {student_id})")
            status = input("Enter Attendance (P/A or leave blank to skip): ").strip().upper()
            if status not in ['P', 'A']:
                status = ""
            new_attendance.append([student_id, name, status, date_today])

    # Include previous records (excluding today's to avoid duplicate)
    previous_records = [r for r in existing_attendance if len(r) == 4 and r[3] != date_today]

    # Write updated attendance
    with open(ATTENDANCE_FILE, mode="w", newline="") as afile:
        writer = csv.writer(afile)
        writer.writerow(header)
        writer.writerows(previous_records + new_attendance)

    print("\n Attendance saved in 'attendance.csv' and returning to main menu.")


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