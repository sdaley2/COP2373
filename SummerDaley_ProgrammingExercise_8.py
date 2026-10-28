import csv

def write_grades():
    """Collect student grades and write them to grades.csv."""

    student_count = int(input("How many students would you like to enter? "))

    # Open the CSV file for writing.
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Write the header row.
        writer.writerow([
            "First Name",
            "Last Name",
            "Exam 1",
            "Exam 2",
            "Exam 3",
        ])

        # Collect and write each student's information.
        for student in range(student_count):
            print(f"\nStudent {student + 1}")

            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            writer.writerow([
                first_name,
                last_name,
                exam1,
                exam2,
                exam3
            ])

def read_grades():
    """Read grades.csv and display the data in tubular format."""

    print("\nStudent Grades")
    print("-" * 60)

    # Open the CSV file for reading.
    with open("grades.csv", "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            print(
                f"{row[0]:<15}"
                f"{row[1]:<15}"
                f"{row[2]:<10}"
                f"{row[3]:<10}"
                f"{row[4]:<10}"
            )

def main():
    """Run the student grade program."""

    write_grades()
    read_grades()

if __name__ == "__main__":
    main()