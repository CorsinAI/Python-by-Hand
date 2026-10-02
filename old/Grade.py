
class Grade:    
    # Plan for this code: 
    # Store names as a alist (Done)
    # Store scores as lists (Done)
    # Have an average function (Done)
    # Have a Letter grading function (Done)
    # Find top score (Done)
    # Use dictionaries instead (In Progress)

    def main(self):
        # list of students
        mylist = ["Alice", "Ben", "Caroline", "Dave", "Esther"]
        # list of grades for every student
        gradesAlice = [4, 2, 4, 5, 6, 6]
        gradesBen = [5, 1, 2, 4, 4, 3]
        gradesCaroline = [4, 5, 5, 2, 3, 4]
        gradesDave = [1, 2, 3, 4, 5, 6]
        gradesEsther = [6 , 5, 6, 4, 3, 5]
        
        # list of grade lists 
        # Note to self this is bad practice and should be done using a different data type probably
        allgrades = [gradesAlice, gradesBen, gradesCaroline, gradesDave, gradesEsther]

        #Loop through the name lists and then print out the average grade for that student
        topscorer = ""
        topscore = 0
        for i in range(len(mylist)):
            if(g.average(allgrades[i]) > topscore):
                topscore = g.average(allgrades[i])
                topscorer = mylist[i]
            print(mylist[i] + " | Average ", end="")
            print(g.average(allgrades[i]) , " | Grade: ", end="")
            print(g.lettergrade(g.average(allgrades[i])))
            print("Hightest scoring Student: " + topscorer + " with grade" , topscore)

    #returns the average of a list
    def average(self, list):
        total = 0
        size = 0
        for element in list:
            size += 1
            total += element
            
        return (round(total / size, 3))
    
    #returns the letter grade based on a double
    def lettergrade(self, double):
        # I could do it as a simple if with lots of cases but that's boring. I'll do it anyway though
        if(double < 4.0):
            return "Failed"
        if(double <= 4.25):
            return "C+"
        if(double <= 4.5):
            return "B-"
        if(double <= 4.75):
            return "B"
        if(double <= 5):
            return "B+"
        if(double <= 5.25):
            return "A-"
        if(double <= 5.5):
            return "A"
        if(double > 5.5):
            return "A+"

    

g = Grade()
g.main()
