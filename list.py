student_name = []
student_grade = []
n = int(input("How many students data you want to enter:"))
for i in range(1,n+1):
    name = input("Enter the name:")
    student_name.append(name)
    grade = input("Enter Grade:")
    student_grade.append(grade)
print()
print("Original List:")
for i in range(0,len(student_name)):
    print(student_name[i],"-",student_grade[i])

def add(name,grade):
    n = input("Enter the name:")
    g = input("Enter the grade:")
    name.append(n)
    grade.append(g)

def update():
    n = input("Enter the student name whose grade you want to update:")
    g = input("Enter new grade:")
    for i in range(0,len(student_name)):
        if(student_name[i] == n):
            student_grade[i] = g
            break

def remove(student_name,student_grade):
    n = input("Enter the student name who you want delete from list:")
    for i in range(0,len(student_name)):
        if(student_name[i] == n):
            del student_name[i]
            del student_grade[i]
            break

def average(student_grade):
    total = len(student_grade)*100
    score = 0
    for i in student_grade:
        if(i == 'A'):
            score += 100
        elif i == 'B':
            score += 80
        else:
            score += 60
    avn = (score/total)*100
    if(avn >= 80):
        print("Average grade:A")
    elif(avn >= 60):
        print("Average grade:B")
    else:
        print("Average grade:C")  


def highlow(student_grade):
    student_grade.sort()
    print("Highest grade:",student_grade[0])
    print("Lowest grade:",student_grade[len(student_grade)-1])

add(student_name,student_grade)
update()
print()
print("**UPDATED LIST**")
for i in range(0,len(student_name)):
    print(student_name[i],"-",student_grade[i])

remove(student_name,student_grade)

print("**UPDATED LIST AFTER DELETION**")
for i in range(0,len(student_name)):
    print(student_name[i],"-",student_grade[i])

average(student_grade)
highlow(student_grade)