# Note:The template file will be copied to a new file. When you change the code of the template file you can create new file with this base code.
from random import randint
def main():
# -----------------------------------Classes-----------------------------------------

    # Defines 'Student' Class
    class Student:
        def __init__(self, id):
            self.id = id
            self.study_group_list =[]
        
        def add_to_study_group_list(self, study_group, number_of_periods):
            if len(self.study_group_list) < number_of_periods:
                self.study_group_list.append(study_group)
            
        def print(self):
            print("student:", self.id, "is in study group(s):", self.study_group_list)

    # Defines 'Conflict' Class
    class Conflict:
        def __init__(self, conflicting_study_group, conflicting_list_of_students):
            self.conflicting_study_group = conflicting_study_group
            self.conflicting_list_of_students = conflicting_list_of_students
            self.number_of_conflicting_students = len(conflicting_list_of_students)

    # Defines 'Period' Class
    class Period:
        def __init__(self,id):
            self.id = id
            self.list_of_study_groups = []
            self.list_of_conflicting_students =[]
            self.number_of_conflicts = 0
             
        def find_conflicts(self):
            for current_study_group in range(0,len(self.list_of_study_groups)):
                for study_group_to_compare in range(0, len(self.list_of_study_groups)):
                    study_group1 = self.list_of_study_groups[current_study_group]
                    study_group2 = self.list_of_study_groups[study_group_to_compare]
                    if current_study_group < study_group_to_compare:
                        conflicting_students = list(set(study_group1.student_list) & set(study_group2.student_list))
                        if len(conflicting_students) > 0:
                            self.number_of_conflicts = self.number_of_conflicts + len(conflicting_students)
                            for student in conflicting_students:
                                self.list_of_conflicting_students.append(student)
        
        def print(self):
            print("Period", self.id,":")
            print("List of Study Groups:", [x.name for x in self.list_of_study_groups])
            print("List of Conflicting Students:", [x.id for x in self.list_of_conflicting_students])
            print("Number of Conflicts:", self.number_of_conflicts)
            print("\n")

    #Defines 'Scenario' Class
    class Scenario:
        def __init__(self, id, period_list):
            self.id = id
            self.period_list = period_list
            self.total_number_of_conflicts = 0

        def calculate_scenarios_total_conflicts(self):
            for period in self.period_list:
                self.total_number_of_conflicts = self.total_number_of_conflicts + period.number_of_conflicts
                
        def print(self):
            print("Scenario",self.id,":")
            print("Total Number of Conflicts:", self.total_number_of_conflicts)
         
    #Defines Study Group Class
    class StudyGroup:
        def __init__(self, name):
            self.name = name
            self.student_list = []
            self.conflicting_study_groupList = []
            self.total_number_of_conflicts = 0
            self.period = 0
        
        def add_student(self, student):
            self.student_list.append(student)
        
        def get_total_conflicts(self):
            self.total_number_of_conflicts = 0
            for study_group in self.conflicting_study_groupList:
                for student in study_group.conflicting_list_of_students:
                    self.total_number_of_conflicts +=1
            return self.total_number_of_conflicts
            
        def print(self):
            print(self.name)
            print("The students in", self.name, "are:",[x.id for x in self.student_list])
            print("Total number of students in", self.name, ":", len(self.student_list))

        def print_conflicts(self):
            print("Total number of conflicts in", self.name, ":", self.get_total_conflicts())
            print("The conflicting study groups with", self.name, "are:\n",[x.conflicting_study_group for x in self.conflicting_study_groupList])
            for conflict_object in self.conflicting_study_groupList:
                print("Students in", self.name," that are also in ", conflict_object.conflicting_study_group,":")
                print([x.id for x in conflict_object.conflicting_list_of_students])
            print("\n") 


# -----------------------------------Functions-----------------------------------------

    def scenarios_generator(list_of_all_study_groups, number_of_periods):
        number_of_study_groups_in_last_period = 0
        scenario_list = []
        scenario_number = 0
        min_conflicts = 2000
        best_scenario_list = []
        number_of_total_study_groups = len(list_of_all_study_groups)

        def create_period_list(number_of_periods):
            listOfPeriods = []
            for num in range(0,number_of_periods):
                listOfPeriods.append(Period(num))
            return listOfPeriods

        def create_scenario(period_list,list_of_all_study_groups):
            for period in period_list:
                for study_group in list_of_all_study_groups:
                    if study_group.period == period.id:
                        period.list_of_study_groups.append(study_group)

                period.find_conflicts()
            return Scenario(scenario_number,period_list)

        # Will continue to run until all the study groups moved into the last period
        while number_of_study_groups_in_last_period != number_of_total_study_groups:
            number_of_study_groups_in_last_period = 0
            i = 0

            while (list_of_all_study_groups[i].period != 0) & (i < number_of_total_study_groups):
                list_of_all_study_groups[i].period = 0
                i+=1
            list_of_all_study_groups[i].period = 1

            period_list = create_period_list(number_of_periods)
            s = create_scenario(period_list,list_of_all_study_groups)
            s.calculate_scenarios_total_conflicts()
            scenario_list.append(s)

            #For Testing
            print("Scenario", scenario_number)
            print("Total Number of Conflicts:",s.total_number_of_conflicts)
            for period in period_list:
                print("Number of Conflicts in Period",period.id,":",period.number_of_conflicts)
                print("Period:",period.id,[x.name for x in period.list_of_study_groups])

            # Finds lowest amount of conflicts
            if s.total_number_of_conflicts < min_conflicts:
                min_conflicts = s.total_number_of_conflicts

            for study_group in range(0, number_of_total_study_groups):
                if list_of_all_study_groups[study_group].period == number_of_periods-1:
                    number_of_study_groups_in_last_period +=1

            #For Testing
            print("number of study groups in period 1:", number_of_study_groups_in_last_period)
            print("length of list of all study groups:", number_of_total_study_groups)
            print("\n")

            scenario_number +=1

        #Finds the Scenarios with the lowest amount of conflicts
        for scenario in scenario_list:
                if scenario.total_number_of_conflicts == min_conflicts:
                    best_scenario_list.append(scenario)
        print("Generated all scenarios!")
        print("Best Scenarios:", [x.id for x in best_scenario_list])
        print("With",min_conflicts,"number of conflicts")
        return scenario_list

    def generate_list_of_students(number_of_students_to_create):
        list_of_all_students = []
        for x in range(1, number_of_students_to_create + 1):
            list_of_all_students.append(Student(x))
        return list_of_all_students

    def generate_study_group_list(list_of_all_study_group_names):
        list_of_all_study_groups = []
        for x in list_of_all_study_group_names:
            list_of_all_study_groups.append(StudyGroup(x))
        return list_of_all_study_groups

    def assign_study_groups_to_students(list_of_students, number_of_periods,list_of_all_study_group_names):
        number_of_students = len(list_of_students)
        for x in range(0,number_of_students):
            study_group = 0
            while study_group < randint(0,number_of_periods):
                list_of_students[x].add_to_study_group_list(
                    list_of_all_study_group_names[
                        randint(0,len(list_of_all_study_group_names)-1)],number_of_periods)
                study_group += 1

    def assign_student_to_study_group(list_of_students, study_group_list):
        for current_study_group in study_group_list:
            for current_student in list_of_students:
                for index in current_student.study_group_list:
                    if index == current_study_group.name:
                        current_study_group.add_student(current_student)

    def get_study_group_conflicts(study_group_list):
        for current_study_group in range(0,len(study_group_list)):
            for study_group_to_compare in range(0, len(study_group_list)):
                study_group1 = study_group_list[current_study_group]
                study_group2 = study_group_list[study_group_to_compare]
                if current_study_group < study_group_to_compare:
                    conflicting_students = list(set(study_group1.student_list) & set(study_group2.student_list))
                    if len(conflicting_students) > 0:
                        study_group1.conflicting_study_groupList.append(Conflict(study_group2.name, conflicting_students))
                        study_group2.conflicting_study_groupList.append(Conflict(study_group1.name, conflicting_students))
                        study_group1.total_number_of_conflicts = study_group1.total_number_of_conflicts + len(conflicting_students)
                        study_group2.total_number_of_conflicts = study_group1.total_number_of_conflicts + len(conflicting_students)


# ------------------------------Functions for Testing--------------------------------

    def print_all_students_info(list_of_students):
        print("PRINTING STUDENTS")
        for student in list_of_students:
            student.print()
        print("FINISHED PRINTING STUDENTS")

    def print_all_study_group_info(study_group_list):
        print("STUDY GROUPS")
        for study_group in study_group_list:
            study_group.print()
            study_group.print_conflicts()
        print("FINISHED PRINTING STUDY GROUPS")

# -----------------------------------Main()-----------------------------------------
    #List of Study Group Names
    #list_of_all_study_group_names = ["Integrated Math", "PreCalc", "Calculus",
                            #   "Stats & Probability", "Physics", "Chemistry",
                            #   "Anatomy", "Biology", "Environmental Science",
                            #   "English 10", "English 11", "English 12", "Vietnamese",
                            #   "Chinese", "Nepali", "STEM Lab", "Art", "Music",
                            #   "Senior Seminar"]


    #For testing
    list_of_all_study_group_names = ["Integrated Math", "PreCalc", "Calculus",
                                "Stats & Probability", "Physics", "Chemistry",
                                "Anatomy", "Biology", "Environmental Science",
                                "English 10"]

    # This will determine how many periods are available
    number_of_periods = 2

    # Generate Students
    number_of_students_to_create = 200
    list_of_students = generate_list_of_students(number_of_students_to_create)

    # Randomly assigns study groups to students.
    # The number of study groups depends on the number of periods
    assign_study_groups_to_students(list_of_students,number_of_periods,list_of_all_study_group_names)

    # Creates a list of study groups based
    # on the array of study group names
    study_group_list = generate_study_group_list(list_of_all_study_group_names)

    # Matches up the students to their randomly assigned study groups
    assign_student_to_study_group(list_of_students, study_group_list)

    # Finds the number of students that are
    # assigned to more than one study group
    get_study_group_conflicts(study_group_list)

    # For testing purposes
    print_all_students_info(list_of_students)
    print_all_study_group_info(study_group_list)

    # Creates every possible scenario by placing every
    # combination of study groups in the given periods
    scenarios_list = scenarios_generator(study_group_list,number_of_periods)

if __name__=="__main__":
    main()



