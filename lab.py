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

