# =================================================================
# PROGRAM: Student Result Management Terminal System (SRMTS)
# FACULTY: Information and Communication Technology
# STUDENT: Yusufu jabbie
# DATE: April 28 2026
# =================================================================

# Global Constant for Student ID prefix [cite: 77, 156]
ID_PREFIX = "905005292"


def get_grade_point(score):
    """
    Module 1: Logic processing for grade points[cite: 69, 81].
    Converts a numerical score into a standard 4.0 scale point.
    """
    if score >= 70:
        return 4.0  # A grade
    elif score >= 60:
        return 3.0  # B grade
    elif score >= 50:
        return 2.0  # C grade
    elif score >= 45:
        return 1.0  # D grade
    else:
        return 0.0  # F grade


def calculate_final_gpa(total_points, count):
    """
    Module 2: Calculations for student GPA[cite: 66, 69].
    Divides total grade points by the number of subjects.
    """
    if count == 0: return 0.0
    return round(total_points / count, 2)


def check_subject_performance(score):
    """
    Module 3: Decision structure for subject status[cite: 67, 79].
    Returns 'PASS' if the score is 50 or above, otherwise 'FAIL'.
    """
    return "PASS" if score >= 50 else "FAIL"


def display_report(name, course, full_id, subject_data, gpa):
    """
    Module 4: Formatted output for the terminal UI[cite: 71, 74].
    Prints the final academic report including the new Course section.
    """
    print("\n" + "=" * 70)
    print(f"OFFICIAL ACADEMIC REPORT: {name.upper()}")
    print(f"COURSE: {course.upper()}")  # New Course Section
    print(f"STUDENT ID: {full_id}")
    print("-" * 70)
    print(f"{'SUBJECT':<30} | {'SCORE':<10} | {'PERFORMANCE':<10}")
    print("-" * 70)

    # Loop through the results to print each module's data [cite: 68, 80]
    for sub, sc, perf in subject_data:
        print(f"{sub:<30} | {sc:<10} | {perf:<10}")

    print("-" * 70)
    print(f"FINAL CALCULATED GPA: {gpa}")
    print("=" * 70)


def main_registration():
    """
    Module 5: Main application loop for data collection[cite: 62, 64].
    Handles user prompts for Name, Course, ID, and Grades.
    """
    # Specific ICT subjects as requested
    subject_list = [
        "Principle of structured Programming",
        "Introduction to Databas",
        "Introduction to Data communication",
        "Software Engineering",
        "Computerized mathematics",
    ]

    print("--- LIMKOKWING SRMTS TERMINAL SYSTEM ---")

    # Input Section [cite: 61, 63]
    name = input("Enter Full Name: ")
    course = input("Enter Course Name (e.g., BSc in Software Engineering): ")

    # ID Validation loop for constant prefix and 4-digit suffix [cite: 68, 77]
    while True:
        id_suffix = input(f"Enter the last 4 digits of ID ({ID_PREFIX}xxxx): ")
        if len(id_suffix) == 4 and id_suffix.isdigit():
            full_id = ID_PREFIX + id_suffix
            break
        else:
            print("Error: Identification must be exactly 4 numbers.")

    total_gp = 0
    performance_records = []

    # Iteration through subjects to collect grades [cite: 68, 80]
    for subject in subject_list:
        try:
            mark = float(input(f"Enter score for {subject}: "))

            # Process performance and points using separate modules [cite: 81]
            perf_status = check_subject_performance(mark)
            total_gp += get_grade_point(mark)

            # Save record in a list [cite: 78]
            performance_records.append((subject, mark, perf_status))

        except ValueError:
            print("Invalid input. Recording 0 for this module.")
            performance_records.append((subject, 0.0, "FAIL"))

    # Final GPA processing [cite: 66]
    final_gpa = calculate_final_gpa(total_gp, len(subject_list))

    # Trigger final output display [cite: 70]
    display_report(name, course, full_id, performance_records, final_gpa)


# Script entry point
if __name__ == "__main__":
    main_registration()