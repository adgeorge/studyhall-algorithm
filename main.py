# Note:The template file will be copied to a new file. When you change the code of the template file you can create new file with this base code.
from random import randint
def main():
#-----------------------------------Classes-----------------------------------------
#-----------------------------------Classes-----------------------------------------
#-----------------------------------Classes-----------------------------------------
    # Defines 'Student' Class
    class Student:
        def __init__(self, id):
            self.id = id
            self.studyGroupList =[]
        
        def addToStudyGroupList(self, studyGroup):
            if len(self.studyGroupList)<2:
                self.studyGroupList.append(studyGroup)
        
        def getId(self):
            return self.id
            
        def print(self):
            print("student:", self.id, "is in study group(s):", self.studyGroupList)
    
            
    # Defines 'Conflict' Class
    class Conflict:
        def __init__(self, conflictingStudyGroup, conflictingListOfStudents):
            self.conflictingStudyGroup = conflictingStudyGroup
            self.conflictingListOfStudents = conflictingListOfStudents
            self.numberOfConflictingStudents = len(conflictingListOfStudents)

    # Defines 'Period' Class
    class Period:
        def __init__(self,id):
            self.id = id
            self.listOfStudyGroups = []
            self.listOfConflictingStudents =[]
            self.numberOfConflicts = 0
             
        def findConflicts(self):
            for currentStudyGroup in range(0,len(self.listOfStudyGroups)):
                for studyGroupToCompare in range(0, len(self.listOfStudyGroups)):
                    studyGroup1 = self.listOfStudyGroups[currentStudyGroup]
                    studyGroup2 = self.listOfStudyGroups[studyGroupToCompare]
                    if currentStudyGroup < studyGroupToCompare:
                        conflictingStudents = list(set(studyGroup1.studentList) & set(studyGroup2.studentList))
                        if len(conflictingStudents) > 0:
                            self.numberOfConflicts = self.numberOfConflicts + len(conflictingStudents)
                            for student in conflictingStudents:
                                self.listOfConflictingStudents.append(student)
        
        def print(self):
            print("Period", self.id,":")
            print("List of Study Groups: ", [x.name for x in self.listOfStudyGroups])
            print("List of Conflicting Students: ", [x.id for x in self.listOfConflictingStudents])
            print("Number of Conflicts: ", self.numberOfConflicts)
            print("\n")

    #Defines 'Scenario' Class
    class Scenario:
        def __init__(self, id, periodList):
            self.id = id
            self.periodList = periodList
            self.totalNumOfConflicts = 0

        def calcTotalConflicts(self):
            for period in self.periodList:
                self.totalNumOfConflicts = self.totalNumOfConflicts + period.numberOfConflicts
            #for period in self.periodList:
             #   self.totalNumOfConflicts = self.totalNumOfConflicts + period.numberOfConflicts
                
        def print(self):
            print("Scenario ",self.id,":")
            print("Total Number of Conflicts: ", self.totalNumOfConflicts)
         
    #Defines Study Group Class
    class StudyGroup:
        def __init__(self, name):
            self.name = name
            self.studentList = []
            self.conflictingStudyGroupList = []
            self.totalNumberOfConflicts = 0
            self.period = 0
        
        def addStudent(self, student):
            self.studentList.append(student)
        
        def getTotalConflicts(self):
            self.totalNumberOfConflicts = 0
            for studyGroup in self.conflictingStudyGroupList:
                for student in studyGroup.conflictingListOfStudents:
                    self.totalNumberOfConflicts +=1
            return self.totalNumberOfConflicts
            
        def print(self):
            print(self.name)
            print("The students in", self.name, "are: ",[x.id for x in self.studentList])
            print("Total number of students in", self.name, ":", len(self.studentList))
        def printConflicts(self):
            print("Total number of conflicts in ", self.name, ":", self.getTotalConflicts())
            print("The conflicting study groups with ", self.name, "are:\n",[x.conflictingStudyGroup for x in self.conflictingStudyGroupList])
            for conflictObject in self.conflictingStudyGroupList:
                print("Students in ", self.name," that are also in ", conflictObject.conflictingStudyGroup,":")
                print([x.id for x in conflictObject.conflictingListOfStudents])
            print("\n") 

#-----------------------------------Functions-----------------------------------------
#-----------------------------------Functions-----------------------------------------
#-----------------------------------Functions-----------------------------------------
    def scenarioGenerator(listOfAllStudyGroups, numberOfPeriods):
        numberOfStudyGroupsInPeriod1 = 0
        scenarioList = []
        scenarioNumber = 0
        minConflicts = 200
        bestScenarioList = []
        while numberOfStudyGroupsInPeriod1 != len(listOfAllStudyGroups):
            numberOfStudyGroupsInPeriod1 = 0
            i = 0
            while (listOfAllStudyGroups[i].period != 0) & (i < len(listOfAllStudyGroups)):
                listOfAllStudyGroups[i].period = 0
                i+=1
            listOfAllStudyGroups[i].period = 1

            listOfPeriods = []
            for num in range(0,numberOfPeriods):
                listOfPeriods.append(Period(num))

#Creates scenarios by adding study groups to their respective period.
            for period in listOfPeriods:
                for studyGroup in listOfAllStudyGroups:
                    if studyGroup.period == period.id:
                        period.listOfStudyGroups.append(studyGroup)

                period.findConflicts()
            s = Scenario(scenarioNumber,listOfPeriods)
            s.calcTotalConflicts()
            scenarioList.append(s)


            #For Testing
            print("Scenario", scenarioNumber)
            print("Total Number of Conflicts:",s.totalNumOfConflicts)
            for period in listOfPeriods:
                #period.findConflicts()
                print("Number of Conflicts in Period ",period.id,":",period.numberOfConflicts)
                print("Period: ",period.id," ",[x.name for x in period.listOfStudyGroups])


            #Finds the best Scenario
            if s.totalNumOfConflicts < minConflicts:
                minConflicts = s.totalNumOfConflicts

            for studyGroup in range(0,len(listOfAllStudyGroups)):
                if listOfAllStudyGroups[studyGroup].period == 1:
                    numberOfStudyGroupsInPeriod1 +=1
            #For Testing
            print("number of study groups in period 1: ", numberOfStudyGroupsInPeriod1)
            print("length of list of all study groups: ", len(listOfAllStudyGroups))
            print("\n")

            scenarioNumber +=1

        #Finds the Scenarios with the lowest amount of conflicts
        for scenario in scenarioList:
                if scenario.totalNumOfConflicts == minConflicts:
                    bestScenarioList.append(scenario)
        print("Best Scenarios: ", [x.id for x in bestScenarioList])
        print("With",minConflicts,"number of conflicts")
        return scenarioList

#-----------------------------------Main()-----------------------------------------
#-----------------------------------Main()-----------------------------------------
#-----------------------------------Main()-----------------------------------------
    #Creates a list of 200 students
    listOfAllStudents = []
    for x in range(1,201):
        listOfAllStudents.append(Student(x))
    
    #List of Study Group Names
    #listOfAllStudyGroupNames = ["Integrated Math", "PreCalc", "Calculus", "Stats & Probability", "Physics", "Chemistry", "Anatomy", "Biology", "Environmental Science", "English 10", "English 11", "English 12", "Vietnamese", "Chinese", "Nepali", "STEM Lab", "Art", "Music", "Senior Seminar"]

    #For testing
    listOfAllStudyGroupNames = ["Integrated Math", "PreCalc", "Calculus", "Stats & Probability", "Physics", "Chemistry", "Anatomy", "Biology", "Environmental Science","English 10"]
    #Assigns randomly 0,1 or 2 study groups to every student     
    for x in range(0,len(listOfAllStudents)):
        i = 0
        while i < randint(0,2):
            listOfAllStudents[x].addToStudyGroupList(listOfAllStudyGroupNames[randint(0, len(listOfAllStudyGroupNames)-1)])
    
    #Prints all the students info
    #print("***********************************PRINTING STUDENTS***************************************")                
    #for x in listOfAllStudents:
        #x.print()
    
    #Creates a list of study groups with names from the list of study group names
    listOfAllStudyGroups = []
    for x in listOfAllStudyGroupNames:
        listOfAllStudyGroups.append(StudyGroup(x))
        
    #Adds all the students to the study group(s) if any 
    #to study groups the student currently has in the study group list
    for currentStudyGroup in listOfAllStudyGroups:
        for currentStudent in listOfAllStudents:
            for index in currentStudent.studyGroupList:
                if index == currentStudyGroup.name:
                    currentStudyGroup.addStudent(currentStudent)
                    
    #Finds all the student intersections between study groups (conflicts)
    #Creates a list of the conflicts
    # Then appends all the conflicts to the conflictList in each studyGroup
    for currentStudyGroup in range(0,len(listOfAllStudyGroups)):
        for studyGroupToCompare in range(0, len(listOfAllStudyGroups)):
            studyGroup1 = listOfAllStudyGroups[currentStudyGroup]
            studyGroup2 = listOfAllStudyGroups[studyGroupToCompare]
            if currentStudyGroup < studyGroupToCompare:
                conflictingStudents = list(set(studyGroup1.studentList) & set(studyGroup2.studentList))
                if len(conflictingStudents) > 0:
                    studyGroup1.conflictingStudyGroupList.append(Conflict(studyGroup2.name, conflictingStudents))
                    studyGroup2.conflictingStudyGroupList.append(Conflict(studyGroup1.name, conflictingStudents))
                    studyGroup1.totalNumberOfConflicts = studyGroup1.totalNumberOfConflicts + len(conflictingStudents)
                    studyGroup2.totalNumberOfConflicts = studyGroup1.totalNumberOfConflicts + len(conflictingStudents)
    #print("***********************************FINISHED PRINTING STUDENTS***************************************")
    print("***********************************STUDY GROUPS***************************************")
    for x in listOfAllStudyGroups:
        x.print()
        x.printConflicts()
    print("***********************************FINISHED GENERATING STUDY GROUPS***************************************")


    scenarioGenerator(listOfAllStudyGroups,2)
    print("Generated all scenarios!")

#NEXT
#Make it so some study groups are larger than others, right now the distribution of students are too evenly disperesed
#Make more students that have similar conflicts (same issure ^^)
#Try creating grade levels so groups of students have similar schedules
#
#next thing to do is sort study groups into first and second period using different sorting algorithm

if __name__=="__main__":
    main()



