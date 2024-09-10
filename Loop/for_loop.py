# Simple 'for' loop
# a = (1, 3, 5, 7, 9)
# for i in a:
#     print(i)

# name = ("Aamer", 5, 3.5, False, True, "Hooria")
# for i in name:
#     print(i)

# Table in 'for' loop
# Table = int(input("Enter your no: "))
# for i in range(1, 11):
#     print(f"{Table} x {i} = {Table * i}")

name = ["Amir", "Aaqib", "Fahad", "Kamran", "Imran"]
for i in name:
    if(i.startswith("A")):
        print(f"Hello {i}")

name = ["Amir", "Aaqib", "Fahad", "Kamran", "Imran"]
for i in name:
    if(i.endswith("n")):
        print(f"Hello {i}")