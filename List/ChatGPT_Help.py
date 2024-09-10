# Initialize empty lists for subjects and marks
subjects = []
marks = []

# Define the number of subjects
num_subjects = 5

# Loop to get subjects and marks from the user
for i in range(num_subjects):
    subject = input(f"Enter the name of subject {i+1}: ")
    mark = int(input(f"Enter the marks for {subject}: "))
    subjects.append(subject)
    marks.append(mark)

# Print each subject with its corresponding mark on a new line
print("Subjects and Marks:")
for subject, mark in zip(subjects, marks):
    print(f"{subject}: {mark}")

# Calculate and print the total score
total_marks = sum(marks)
print("Your total score is:", total_marks)