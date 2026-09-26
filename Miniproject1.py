#count the number of students in a class
numberofstudents = int(input("Total number of records : "))

#data storage 
studentsdata = []

# printing students data
for i in range(numberofstudents):
    print(f"Enter the students data {i + 1}")
    name = input("Name : ")
    rollnumber = int(input("Roll Number :"))
    marks = int(input("marks : "))
    
    if marks > 95:
        grade = "A"
    elif marks > 70:
        grade = "B"
    elif marks > 35:
        grade = "C"
    else:
        grade = "F"
        
    students = {
            "Name" : name,
            "Roll number" : rollnumber,
            "marks" : marks,
            "grade" : grade 
        }   

    studentsdata.append(students)
 
 
#Data printing
print("\nStudents data is : ")

for s in studentsdata:
    print(f"Name : {s['Name']} -" f" Roll Number : {s['Roll number']} -" f" marks : {s['marks']} -" f" Grade : {s['grade']}")

#students who passed the exam
print("\nStudents who passed the exam are : ")

for s in (studentsdata):
    if s['marks'] > 33:
        print(f"{s['Name']} - marks : {s['marks']}")
        
      
 
 
