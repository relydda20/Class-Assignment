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
        self.__Courses = str(courses)
        self.__grades = int(grades)
    
    def addCourseGrade(self, courses, grades):
        self.__courses = courses
        self.__grades = grades

    def printGrades(self):
        print(self.__grades)

    def getAverageGrade(self):
        return sum(self.__grades) / len(self.__grades)

    def toString(self):
        return f"The name is {self.getName()}, The adress is {self.getAdress()}."

class Teacher(Person):
    def __init__(self, name, adress, numCourses = 0, courses =[]):
        super().__init__(name, adress)
        self.__numCourses = 0
        self.__courses = []

    def addCourse(self, course):
        for courses in self.__courses:
            if course == courses:
                return False
        self.__courses.append(course)
        return True
    
    def removeCourse(self, course):
        if course in self.__courses:
            self.__courses.remove(course)
            return True
        else:
            return False
    
    def toString(self):
        return f"The name is {self.getName()}, The adress is {self.getAdress()}."
