# --------------------------------------------
# Name:
# Date:
# Program: Chapter 6 Practice
# Description:
# Complete each section by following the
# directions in the comments.
# --------------------------------------------


# ------------------------------------------------
# Practice 1: Writing to a File
# ------------------------------------------------
# TODO:
# 1. Open a file named "data.txt" in write ('w') mode
# 2. Write your name to the file
# 3. Write your favorite number on the next line
# 4. Close the file

print()  # blank line


# ------------------------------------------------
# Practice 2: Reading from a File
# ------------------------------------------------
# TODO:
# 1. Open "data.txt" in read ('r') mode
# 2. Read the contents of the file
# 3. Print the contents to the screen
# 4. Close the file

print()


# ------------------------------------------------
# Practice 3: Reading with a Loop
# ------------------------------------------------
# TODO:
# 1. Open "data.txt" in read mode
# 2. Use a loop to read each line in the file
# 3. Strip the newline character using rstrip()
# 4. Print each line
# 5. Close the file

print()


# ------------------------------------------------
# Practice 4: Writing and Reading Numbers
# ------------------------------------------------
# TODO:
# 1. Open a file named "numbers.txt" in write mode
# 2. Write 3 numbers to the file (each on a new line)
#    (Hint: convert numbers to strings)
# 3. Close the file
#
# 4. Open "numbers.txt" in read mode
# 5. Read each number using a loop
# 6. Convert each value back to an integer
# 7. Add the numbers together
# 8. Print the total
# 9. Close the file

print()


# ------------------------------------------------
# Practice 5: Debug the Exception
# ------------------------------------------------
# TODO:
# The program below is supposed to:
# - Ask the user for a filename
# - Open the file
# - Display its contents
#
# There are 3 errors in this code.
# Fix them so the program works correctly.


filename = input("Enter a filename: ")

try
    file = open(filename, 'r')
    contents = file.read()
    print(contents)

except
    print("Error reading file")

file.close()
