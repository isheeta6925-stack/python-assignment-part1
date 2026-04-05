# 1: cleaning student data
data = [
 {"name": " Ayesha Sharma ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
 {"name": " Rohit Verma", "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
 {"name": " Priya Nair ", "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
 {"name": " Karan Mehta ", "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
 {"name": " Sneha Pillai ", "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]
students = []

for student in data:
   # basic cleaning
   name = student ["name"].strip().title()
   roll = int(student["roll"])
   # splitting the string and turning into ints
   marks = [int(m) for m in student["marks_str"].split(", ")]

   # creating a clean dictionary
   info = {"name": name, "roll": roll, "marks": marks}
   students.append(info)

   # check if name is only letters
   check_name = all(x.isalpha() for x in name.split())
   valid_msg = "✓ Valid name" if check_name else "✗ Invalid name"

   print("---")
   print(f"Name: {name} | {valid_msg}")
   print(f"Roll: {roll}")
   print(f"Marks: {marks}")

# special check for Roll 103
for s in students:
   if s["roll"] == 103:
     print(f"\n[Roll 103] Upper: {s['name'].upper()}")
     print(f"[Roll 103] Lower: {s['name'].lower()}")

# 2: marks analysis

print("\n*2: Analysing marks*")

st_name = "Ayesha Sharma"
subs = ["Math", "Physics", "CS", "English", "Chemistry"]
marks_val = [88, 72, 95, 60, 78]

# help function for grades
def find_grade(marks):
 if marks>= 90: return "A+"
 if marks>= 80: return "A"
 if marks>= 70: return "B"
 if marks>= 60: return "C"
 return "F"

print(f"\nReport for {st_name}:")
for i in range(len(subs)):
 g = find_grade(marks_val[i])
 print(f"{subs[i]:<10}:{marks_val[i]}->({g})")

# basic math
total = sum(marks_val)
avg = round(total / len(marks_val), 2)
best = subs[marks_val.index(max(marks_val))]
worst = subs[marks_val.index(min(marks_val))]

print(f"\nTotal:{total}")
print(f"Average:{avg}")
print(f"Best in:{best} ({max(marks_val)})")
print(f"Lowest in:{worst} ({min(marks_val)})")

print("\n-Add More Subjects-")
extra_subs = []
extra_marks = []

while True:
    sub = input("Subject name (or 'done'):").strip()
    if sub.lower() == "done":
        break

    try:
        m = int(input(f"Marks for {sub}:"))
        if 0 <= m <= 100:
            extra_subs.append(sub)
            extra_marks.append(m)
            print(f"Added {sub}!")
        else:
            print("Marks should be 0-100!")
    except ValueError:
        print("Please enter a number!")

all_marks = marks_val + extra_marks
new_avg = round(sum(all_marks) / len(all_marks), 2)
print(f"Updated Average: {new_avg}")

# 3: class summary

print("\n-3: CLASS SUMMARY-")

class_data = [
 ("Ayesha Sharma", [88, 72, 95, 60, 78]),
 ("Rohit Verma", [55, 68, 49, 72, 61]),
 ("Priya Nair", [91, 85, 88, 94, 79]),
 ("Karan Mehta", [40, 55, 38, 62, 50]),
 ("Sneha Pillai", [75, 80, 70, 68, 85]),
]
passed = 0
failed = 0
all_avgs = []
topper = ""
top_marks = 0

for name, scores in class_data:
    avg = round(sum(scores)/len(scores),2)
    all_avgs.append(avg)
    
    if avg>=60:
        result="Pass"
        passed+=1
    else:
        result="Fail"
        failed+=1
    
    if avg > top_marks:
        top_marks=avg
        topper=name
    
    print(f"{name:<18}|{avg:<7}|{result}")

class_avg = round(sum(all_avgs)/len(all_avgs),2)
print(f"\nPassed:{passed}|Failed:{failed}")
print(f"Topper:{topper}({top_marks})")
print(f"Class Average:{class_avg}")

# 4: string work

print("\n-4:String Work-")

txt = "python is a versatile language. It supports object-oriented, functional, and procedural programming. python is widely used in data science and machine learning."

# cleaning the text
clean_txt = txt.strip()
print(f"\nCleaned:\n{clean_txt}")
print(f"\nTitle Case:\n{clean_txt.title()}")

# counting & replacing
count_py = clean_txt.count("python")
print(f"\n'python' appears {count_py} times.")

new_txt = clean_txt.replace("python", "Python 🐍")
print(f"\nUpdated text:\n{new_txt}")

# splitting into sentences
bits = clean_txt.split(". ")
print("\nSentence list:")
print(bits)

print("\nNumbered list:")
for num, line in enumerate(bits, 1):
    line = line.strip()
    if not line.endswith("."):
        line += "."
    print(f"{num}. {line}")

