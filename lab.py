# ▶️ 1. Creating Variables and Assigning Values
name = "Abdulrahim"
age = 35
height = 1.75  # in meters
is_student = False

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)

# ✅ Task 1: Create variables for your city (string), number of kids (int), and has_pet (boolean)
city = "Vancouver"
num_kids = 2
has_pet = True


print("\nYour city:", city)
print("Number of kids:", num_kids)
print("Has pet:", has_pet)

# ▶️ 2. Reassigning Variables
age = 36  # Happy birthday!
print("\nNew age after birthday:", age)

# ✅ Task 3: Calculate the age your kids will be in 5 years and print
kids_age_in_5_years = num_kids + 5  # Assuming num_kids is the total number, change logic as needed
print("Kids' age in 5 years (assuming starting age = num_kids):", kids_age_in_5_years)

# ▶️ 4. Data Types Check
print("\nType of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))

# ✅ Task 4: Print the data type of your city, num_kids, and has_pet variables
print("Type of city:", type(city))
print("Type of num_kids:", type(num_kids))
print("Type of has_pet:", type(has_pet))

# ▶️ 5. String Concatenation Using Variables
greeting = "Hello, my name is " + name + " and I live in " + city + "."
print("\n" + greeting)


# ✅ Task 5: Create a sentence introducing yourself using your variables and print it
my_intro = f"My name is {name}, I am {age} years old, and I live in {city}."
print(my_intro)

# ▶️ 1. Creating a List of Lists (2D List)
# Let's say we have student scores for 3 students in 3 subjects
scores = [
    [85, 92, 78],   # Student 1
    [76, 88, 90],   # Student 2
    [90, 91, 95]    # Student 3
]
print("Initial scores:", scores)

# ▶️ 2. Accessing Elements
print("Score of Student 1 in Subject 2:", scores[0][1])  # 92

# ✅ Task 1: Print score of Student 3 in Subject 3
print("Student 3, Subject 3:", scores[2][2])

# ▶️ 3. Iterating through a List of Lists
print("All scores row by row:")
for student_scores in scores:
    print(student_scores)

# ✅ Task 2: Print each individual score in a tabular format
print("Individual scores:")
for i, student_scores in enumerate(scores):
    for j, score in enumerate(student_scores):
        print(f"Student {i+1}, Subject {j+1}: {score}")

# ▶️ 4. Adding a New Student's Scores
scores.append([88, 79, 85])
print("After adding Student 4:", scores)

# ✅ Task 3: Add another student with scores [70, 80, 90]
scores.append([70, 80, 90])
print("After adding Student 5:", scores)

# ▶️ 5. Updating a Value
# Let's update Student 2's score in Subject 1 to 95
scores[1][0] = 95
print("After updating Student 2's Subject 1 score:", scores)

# ✅ Task 4: Change Student 5's Subject 2 score to 82
scores[4][1] = 82
print("After updating Student 5's Subject 2 score:", scores)

# ▶️ 6. Calculating Averages
print("Average score per student:")
for i, student_scores in enumerate(scores):
    avg = sum(student_scores) / len(student_scores)
    print(f"Student {i+1} average: {round(avg, 2)}")

# ✅ Task 5: Print subject-wise average (column-wise average)
print("Average score per subject:")
num_subjects = len(scores[0])
num_students = len(scores)

for subj in range(num_subjects):
    total = sum(scores[student][subj] for student in range(num_students))
    avg = total / num_students
    print(f"Subject {subj+1} average: {round(avg, 2)}")

# ▶️ 7. Flattening a List of Lists into a Single List
all_scores = [score for student in scores for score in student]
print("All scores flattened:", all_scores)

# ✅ Task 6: Find the highest score among all students
highest = max(all_scores)
print("Highest score among all students:", highest)

import numpy as np
# ---------------------------------------------
# 1. Creating Arrays
# ---------------------------------------------

# Create a 1D array from a list
a = np.array([1, 2, 3])
print("1D Array:", a)

# Create a 2D array (matrix)
b = np.array([[1, 2], [3, 4]])
print("2D Array:\n", b)

# ---------------------------------------------
# 2. Array Properties
# ---------------------------------------------

print("Shape:", a.shape)
print("Dimensions:", a.ndim)
print("Data type:", a.dtype)
print("Total elements:", a.size)

# 3. Special Arrays
# ---------------------------------------------

print("Zeros:\n", np.zeros((2, 3)))
print("Ones:\n", np.ones((3, 3)))
print("Full with 7s:\n", np.full((2, 2), 7))
print("Identity Matrix:\n", np.eye(3))
print("Range with step:\n", np.arange(0, 10, 2))
print("Evenly spaced:\n", np.linspace(0, 1, 5))

# 4. Reshaping & Flattening
# ---------------------------------------------

arr = np.arange(1, 7)
reshaped = arr.reshape((2, 3))
print("Reshaped 2x3:\n", reshaped)
print("Flattened:", reshaped.flatten())

# 5. Indexing & Slicing
# ---------------------------------------------

matrix = np.array([[10, 20, 30], [40, 50, 60]])
print("Element at row 1, col 2:", matrix[1, 2])
print("Second column:", matrix[:, 1])
print("Submatrix (rows 0-1, cols 1-2):\n", matrix[0:2, 1:3])

# 6. Element-wise Operations
# ---------------------------------------------

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print("Add:", x + y)
print("Multiply:", x * y)
print("Square root:", np.sqrt(x))
print("Exponential:", np.exp(x))
print("Log:", np.log(x))

# 7. Matrix Multiplication
# ---------------------------------------------

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[2, 0], [1, 3]])
product = np.dot(m1, m2)
print("Matrix Product:\n", product)

# ---------------------------------------------
# 8. Aggregate Functions
# ---------------------------------------------

stats = np.array([[5, 10, 15], [20, 25, 30]])
print("Sum:", stats.sum())
print("Mean:", stats.mean())
print("Std Dev:", stats.std())
print("Min:", stats.min())
print("Max:", stats.max())
print("Column-wise sum:", stats.sum(axis=0))
print("Row-wise sum:", stats.sum(axis=1))

# 9. Boolean Filtering
# ---------------------------------------------

data = np.array([10, 20, 30, 40, 50])
mask = data > 30
print("Mask:", mask)
print("Filtered Data:", data[mask])







