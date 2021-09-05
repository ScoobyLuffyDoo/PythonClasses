#===============================================================================
# CLASSES
#===============================================================================
# Basic class with variable and Function 
class basicClass:
    Variable ="my Variable in my Class 1"
    def function(self):
        print(Variable)

# Basic class with Constructor and Function 
class basicClassConstructor:
    # A default Constructor
    def __init__(self,Variable1,Variable2):
        self.Variable1 = Variable1
        self.Variable2 = Variable2
    def function(self):
        return ("This is {} and {} in a function using a the class constructor (reserved method) ". format(self.Variable1, self.Variable2))

# Class with Constructor and function and Variables 
class everythigClass:
    ClassVar1 = "Class Variable 1"
    ClassVar2 = "Class Variable 2"
    

    def __init__(self,ConstructVar1,ConstructVar2):
        self.ConstructVar1 = ConstructVar1
        self.ConstructVar2 = ConstructVar2


    def everything_function(self,VarParm1, VarParm2):
        return ("This is is the Class constructor varable 1 and 2 {0}, {1} \n"
                "This is the function paramater variable 1 and 2 {2} ,{3}"
        ).format(self.ConstructVar1, self.ConstructVar2 ,VarParm1 ,VarParm2) 

#=================================================
# OBJECTS
#=================================================
    #Assigning Object with Class
mybasicObject = basicClass()
#=================================================
# MAIN 
#=================================================
# Basic Class with variable 
print(mybasicObject.Variable)
#-----------------
# Basic Class Constructor 
Variable1 = "var1"
Variable2 = "var2"
print(basicClassConstructor(Variable1,Variable2).function())
#-----------------
# Class with everyting 
myEverything = everythigClass("CtrVar1","CtrVar2",).everything_function("VarParm1","VarParm2")
print(myEverything)


