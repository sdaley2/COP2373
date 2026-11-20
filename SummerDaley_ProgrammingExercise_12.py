import numpy as np

def load_grades():
    """Load exam grades from the grades.csv file."""

    grades = np.genfromtxt('grades.csv', delimiter=',', skip_header=1, usecols=(2, 3, 4))

    return grades

def display_exam_statistics(grades):
    """Calculate and display statistics for each exam."""

    print("\nExam Statistics")
    print("-" * 50)

    for exam in range(3):
        exam_grades = grades[:, exam]

        print(f"\nExam {exam + 1}")
        print(f"Mean: {np.mean(exam_grades):.2f}")
        print(f"Median: {np.median(exam_grades):.2f}")
        print(f"Standard Deviation: {np.std(exam_grades):.2f}")
        print(f"Minimum: {np.min(exam_grades):.2f}")
        print(f"Maximum: {np.max(exam_grades):.2f}")

def display_overall_statistics(grades):
    """Calculate and display statistics for all exam grades."""

    print("\nOverall Statistics")
    print("-" * 50)

    print(f"Mean: {np.mean(grades):.2f}")
    print(f"Median: {np.median(grades):.2f}")
    print(f"Standard Deviation: {np.std(grades):.2f}")
    print(f"Minimum: {np.min(grades):.2f}")
    print(f"Maximum: {np.max(grades):.2f}")

def display_pass_fail(grades):
    """Display the number of students who passed and failed each exam."""

    print("\nPass/Fail Results")
    print("-" * 50)

    for exam in range(3):
        exam_grades = grades[:, exam]

        passed = np.sum(exam_grades >= 60)
        failed = np.sum(exam_grades < 60)

        print(f"\nExam {exam + 1}")
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")

    total_grades = grades.size
    total_passed = np.sum(grades >= 60)

    pass_percentage = (total_passed / total_grades) * 100

    print(f"\nOverall Pass Percentage: {pass_percentage:.2f}%")

def main():
    """Run the student grade analysis program."""

    grades = load_grades()

    print("First few rows of grade data")
    print("-" * 50)
    print(grades[:5])

    display_exam_statistics(grades)
    display_overall_statistics(grades)
    display_pass_fail(grades)

if __name__ == "__main__":
    main()

