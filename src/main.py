import csv
import os
from datetime import datetime




STUDENT_FILE = "students.csv"
ATTENDANCE_FILE = "attendance.csv"

def mark_attendance():
    if not os.path.exists(STUDENT_FILE):
        print(" Student file not found.")

def generate_report():
    
    ATTENDANCE_FILE = "attendance.csv"

    if not os.path.exists(ATTENDANCE_FILE):
        print("Attendance file not found.")

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

=======
    header = rows[0]
    data_rows = rows[1:]

    # Counters
    present_count = 0
    absent_count = 0
    no_entry_count = 0

    # -- Clean and process attendance values
    cleaned_rows = []
    for row in data_rows:
        if len(row) < 4 or row[0].strip().lower() == "id":
            continue  # Skip malformed or duplicate header rows

        status = row[2].strip().lower()

        if not status:
            row[2] = "No Entry"
            no_entry_count += 1
        elif status in ("p", "present"):
            row[2] = "Present"
            present_count += 1
        elif status in ("a", "absent"):
            row[2] = "Absent"
            absent_count += 1
        else:
            row[2] = "No Entry"
            no_entry_count += 1

        cleaned_rows.append(row)

    # -- Display the report
    print("\n Attendance Report:\n")
    print(f"{'ID':<10} {'Name':<20} {'Attendance':<15} {'Date':<12}")
    print("-" * 60)
    for row in cleaned_rows:
        print(f"{row[0]:<10} {row[1]:<20} {row[2]:<15} {row[3]:<12}")

    # -- Print summary just below the table
    print("-" * 60)
    print(f"{'Summary':<10}")
    print(f"{'Present':<10}: {present_count}")
    print(f"{'Absent':<10}: {absent_count}")
    print(f"{'No Entry':<10}: {no_entry_count}")

    # -- Save report to a new file
    report_filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(report_filename, mode="w", newline="") as rfile:
        writer = csv.writer(rfile)
        writer.writerow(header)
        writer.writerows(cleaned_rows)

    print(f"\nReport saved as: {report_filename}")

    # -- Clear the attendance.csv file (keep only header)
    with open(ATTENDANCE_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)


    print("attendance.csv has been cleared.\n")
    
    
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