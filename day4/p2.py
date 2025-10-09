marks = {"alice": 85, "bob": 90, "charlie": 78, "david": 88}

for student, mark in marks.items():
    print(f"{student}: {mark}")

top_student = max(marks, key=marks.get)
print(f"Top student: {top_student} {marks[top_student]} marks")

average = sum(marks.values()) / len(marks)
print(f"Average marks: {average:.2f}")
