import csv
import os
from datetime import datetime

ATTENDANCE_FILE = "attendance.csv"

def generate_report():
    if not os.path.exists(ATTENDANCE_FILE):
        print("Attendance file not found.")
        return

    # -- Load the attendance data
    with open(ATTENDANCE_FILE, mode="r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) < 2:
        print("No attendance data found.")
        return

    header = rows[0]
    data_rows = rows[1:]

    # Replace empty Attendance with "No Entry"
    for row in data_rows:
        if len(row) < 4:
            continue
        if not row[2].strip():
            row[2] = "No Entry"

    # -- Display the report
    print("\n Attendance Report:\n")
    print(f"{'ID':<10} {'Name':<20} {'Attendance':<15} {'Date':<12}")
    print("-" * 60)
    for row in data_rows:
        if len(row) < 4:
            continue
        print(f"{row[0]:<10} {row[1]:<20} {row[2]:<15} {row[3]:<12}")

    #-- Save report to a new file
    report_filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(report_filename, mode="w", newline="") as rfile:
        writer = csv.writer(rfile)
        writer.writerow(header)
        writer.writerows(data_rows)

    print(f"\n Report saved as: {report_filename}")

    # Clear the attendance.csv file
    with open(ATTENDANCE_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)  
        
    # Keep header, clear data
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