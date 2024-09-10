# Grade wise Result
print("Humayoon New Era Public School")
Name = input("Enter your name: ")
marks1 = int(input("Enter your 1st subject marks: "))
marks2 = int(input("Enter your 2nd subject marks: "))
marks3 = int(input("Enter your 3rd subject marks: "))
marks4 = int(input("Enter your 4th subject marks: "))
marks5 = int(input("Enter your 5th subject marks: "))

total_percentage = (100*(marks1+marks2+marks3+marks4+marks5))/500
if(total_percentage<=100 and total_percentage>=90):
    grade = "A1"
    print("You are topper with grade",[grade], total_percentage,"%")
    print("Congratulations!")
elif(total_percentage<90 and total_percentage>80):
    grade = "A"
    print("You are best with grade",[grade], total_percentage,"%")
    print("Congratulations!")
elif(total_percentage<80 and total_percentage>70):
    grade = "B"
    print("You are pass with grade:",[grade], total_percentage,"%")
    print("You can do more better!")
elif(total_percentage<70 and total_percentage>60):
    grade = "C"
    print("You are just pass with",[grade], total_percentage,"%")
    print("You need to work hard!")
else:
    print("You are fail, try again", total_percentage,"%")