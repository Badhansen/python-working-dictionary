n = int(input())
student = []
grade = []

for i in range(n):
    student.append(input())
    grade.append(float(input()))

m = min(grade)

for x in range(n):
    if grade[x] == m:
        grade[x] = 100000000.00

m = min(grade)

lst = []

for x in range(n):
    if grade[x] == m:
        lst.append(student[x])

lst.sort()

for x in range(len(lst)):
    print(lst[x])

