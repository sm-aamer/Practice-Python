# Percentage with Marks condition

marks1 = int(input("Enter your 1st subject marks: "))
marks2 = int(input("Enter your 2nd subject marks: "))
marks3 = int(input("Enter your 3rd subject marks: "))
marks4 = int(input("Enter your 4th subject marks: "))
marks5 = int(input("Enter your 5th subject marks: "))
total_percentage = (100*(marks1+marks2+marks3+marks4+marks5))/500
if(total_percentage>=40 and marks1>=40 and marks2>=40 and marks3>=40 and marks4>=40 and marks5>=40):
    print("You are pass:", total_percentage, "%")
    print("Congratulations!")

else:
    print("You are fail, try again", total_percentage, "%")