Subject = []
Marks = []

a = input("Enter your 1st subject here: ")
b = int(input("Enter your marks here: "))
Subject.append(a)
Marks.append(b)

c = input("Enter your 2nd subject here: ")
d = int(input("Enter your marks here: "))
Subject.append(c)
Marks.append(d)

e = input("Enter your 3rd subject here: ")
f = int(input("Enter your marks here: "))
Subject.append(e)
Marks.append(f)

g = input("Enter your 4th subject here: ")
h = int(input("Enter your marks here: "))
Subject.append(g)
Marks.append(h)

i = input("Enter your 5th subject here: ")
j = int(input("Enter your marks here: "))
Subject.append(i)
Marks.append(j)

print("\nYour scored the marks in the subject are noted against each:-\n")
print(Subject[0], Marks[0])
print(Subject[1], Marks[1])
print(Subject[2], Marks[2])
print(Subject[3], Marks[3])
print(Subject[4], Marks[4])
print("Your total score is:", sum(Marks))