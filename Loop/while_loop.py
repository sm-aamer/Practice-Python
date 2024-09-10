# Print all items, using the while loop 
list = ["apple", "banana", "cherry"]
i = 0
while i <len(list):
  print(list[i])
  i = i + 1

# Exit the loop when i is 3
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
# Continue to the next iteration if i is 3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
# Print a message once the condition is false:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("Loop is over now")

# Table in 'for' loop
Table = int(input("Enter your no: "))
i = 1
while i<11:
    print(f"{Table} x {i} = {Table * i}")
    i +=1
