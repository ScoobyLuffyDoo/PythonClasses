# Formating Student Details 
class Student:
    SchoolName ="Blha High"
    # A default Constructor
    def __init__(self,Name,Surname,Age,StudentID):
        self.Name = Name
        self.Surname = Surname
        self.Age = Age
        self.StudentID = StudentID
    # Summery of the student
    def StudentDetails(self):
        #Createing Student Summery
        studentinfo = ("{} : The Students name is {} {} and he or she is {} years old ".format( self.StudentID, self.Name, self.Surname, self.Age))
        return studentinfo
    print("This student is in "+SchoolName)
        
# Giving my Student details 
StudentName = "Simone"
StudentSurname ="Smal"
StudentAge = 21
StudentStudentID = "SI21SM"
# Assigning Student class to an object 
myStudent = Student(StudentName,StudentSurname,StudentAge,StudentStudentID)


#getting student details Summery 

print(str(myStudent.StudentDetails()))