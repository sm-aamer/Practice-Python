a = "Make money online"
b = "Order Now"
c = "Click now"
d = "see more"

comments = input("Enter your comments: ")
if((a in comments) or (b in comments) or (c in comments) or (d in comments)):
    print("This is an spam")
    print("Beware of spam")

else:
    print("Your comments has been saved")
    print("Thank You")