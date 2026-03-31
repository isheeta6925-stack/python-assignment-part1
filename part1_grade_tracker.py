# task 1 - parse and clean student data

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

for student in raw_students:
    clean_name  = student["name"].strip().title()
    clean_roll  = int(student["roll"])
    clean_marks = [int(m) for m in student["marks_str"].split(", ")]

    cleaned = {
        "name":  clean_name,
        "roll":  clean_roll,
        "marks": clean_marks
    }
    cleaned_students.append(cleaned)

    is_valid = all(word.isalpha() for word in clean_name.split())
    validity = "✓ Valid name" if is_valid else "✗ Invalid name"

    print("======")
    print(f"Student : {clean_name}   {validity}")
    print(f"Roll No : {clean_roll}")
    print(f"Marks   : {clean_marks}")
    print("======")

for s in cleaned_students:
    if s["roll"] == 103:
        print(f"\nStudent Roll 103 - ALL CAPS : {s['name'].upper()}")
        print(f"Student Roll 103 - lowercase : {s['name'].lower()}")


# task 2 - marks analysis

print("\n======")
print("TASK 2 - Marks Analysis")
print("======")

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks    = [88, 72, 95, 60, 78]

def get_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"

print(f"\nGrade Report for {student_name}:")
for subject, mark in zip(subjects, marks):
    grade = get_grade(mark)
    print(f"  {subject:<12} : {mark}  -> Grade: {grade}")

total   = sum(marks)
average = round(total / len(marks), 2)
highest_subject = subjects[marks.index(max(marks))]
lowest_subject  = subjects[marks.index(min(marks))]

print(f"\nTotal Marks   : {total}")
print(f"Average Marks : {average}")
print(f"Highest Score : {highest_subject} ({max(marks)})")
print(f"Lowest Score  : {lowest_subject} ({min(marks)})")

print("\n--- New Subject Entry System ---")
print("Type 'done' to stop adding subjects.\n")

new_subjects = []
new_marks    = []

while True:
    subject_input = input("Enter subject name (or 'done' to stop): ").strip()
    if subject_input.lower() == "done":
        break

    marks_input = input(f"Enter marks for {subject_input} (0-100): ").strip()

    try:
        marks_value = float(marks_input)
        if not (0 <= marks_value <= 100):
            print("⚠ Warning: Marks must be between 0 and 100. Entry skipped.")
            continue
        new_subjects.append(subject_input)
        new_marks.append(int(marks_value))
        print(f"  ✓ Added {subject_input} with marks {int(marks_value)}")
    except ValueError:
        print("⚠ Warning: Invalid input — please enter a number. Entry skipped.")

print(f"\nNew subjects added: {len(new_subjects)}")

all_marks       = marks + new_marks
updated_average = round(sum(all_marks) / len(all_marks), 2)
print(f"Updated average across all subjects: {updated_average}")


# task 3 - class performance summary

print("\n=====")
print("TASK 3 - Class Performance Summary")
print("=====")

class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma",   [55, 68, 49, 72, 61]),
    ("Priya Nair",    [91, 85, 88, 94, 79]),
    ("Karan Mehta",   [40, 55, 38, 62, 50]),
    ("Sneha Pillai",  [75, 80, 70, 68, 85]),
]

print(f"\n{'Name':<18} | {'Average':^7} | Status")
print("-" * 40)

passed_count = 0
failed_count = 0
averages     = []
topper_name  = ""
topper_avg   = 0

for name, m in class_data:
    avg    = round(sum(m) / len(m), 2)
    status = "Pass" if avg >= 60 else "Fail"
    averages.append(avg)

    if status == "Pass":
        passed_count += 1
    else:
        failed_count += 1

    if avg > topper_avg:
        topper_avg  = avg
        topper_name = name

    print(f"{name:<18} | {avg:^7.2f} | {status}")

class_average = round(sum(averages) / len(averages), 2)

print(f"\nStudents Passed : {passed_count}")
print(f"Students Failed : {failed_count}")
print(f"Class Topper    : {topper_name} (Average: {topper_avg})")
print(f"Class Average   : {class_average}")


# task 4 - string manipulation

print("\n=====")
print("TASK 4 - String Manipulation")
print("======")

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

clean_essay = essay.strip()
print(f"\nStep 1 - Stripped Essay:\n{clean_essay}")

print(f"\nStep 2 - Title Case:\n{clean_essay.title()}")

python_count = clean_essay.count("python")
print(f"\nStep 3 - Count of 'python': {python_count}")

replaced = clean_essay.replace("python", "Python 🐍")
print(f"\nStep 4 - Replaced:\n{replaced}")

sentences = clean_essay.split(". ")
print(f"\nStep 5 - Sentences list:\n{sentences}")

print("\nStep 6 - Numbered Sentences:")
for i, sentence in enumerate(sentences, 1):
    if not sentence.endswith("."):
        sentence = sentence + "."
    print(f"{i}. {sentence}")