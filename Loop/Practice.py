Subjects=[]
Marks=[]

name=input("Enter your name: ")

i=0
while(i<2):
    subject = input(f"Enter your {i} subject: ")
    mark = int(input("Enter your marks: "))
    Subjects.append(subject)
    Marks.append(mark)
    i +=1
marks_obtained = sum(Marks)
total_marks=200

result = (marks_obtained / total_marks)*100
print(f"The result of Mr {name}")
print(Subjects, Marks)
print(f"Total Marks Obtained: {marks_obtained}")
print(result,"%")
# print(f"Student Name: {name}")
# print(f"Subjects and Marks: {list(zip(Subjects, Marks))}")
# print(f"Total Marks Obtained: {marks_obtained}")
# print(f"Percentage: {result:.2f}%")