class Person:
    def __init__(self, name, adress):
        self.__name = str(name)
        self.__adress = str(adress)
    
    def getName(self):
        return self.__name

    def getAdress(self):
        return self.__adress
    
    def setAdress(self, adress):
        self.__adress = adress
    
    def toString(self):
        return f"The name is {self.getName()}, the adress is {self.setAdress()}."

class Student(Person):
    def __init__(self, name, adress, numCourses = 0, courses = [], grades =[]):
        super().__init__(name, adress)
        self.__numCourses = int(numCourses)
        self.__courses = str(courses)
        self.__grades = int(grades)
    
    def addCourseGrade(self, courses, grades):
        self.__courses = courses
        self.__grades = grades

    def printGrades(self):
        print(self.__grades)

    def getAverageGrade(self):
        return sum(self.__grades) / len(self.__grades)