file = open("second homework/students_names.txt","r+")
content = file.read()
more_students =["Yanis","Kouciela","Malek"]
for student in more_students :
    if (student == more_students[0]):
        new_content = content + "\n" + student
    else:
        new_content = new_content + "\n" + student
    file.write("\n")
    file.write(student)
print(content)
print(more_students)
print("Yanis" in new_content)
file.close()


file2 = open("second homework/newFile.txt", "w")
Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for letter in Alphabet :
    file2.write(letter)
    file2.write(".txt")
    file2.write("\n")
file2.close()