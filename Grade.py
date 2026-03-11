
class Grade:    
    def main(self):
        # list of students
        mylist = ["Alice", "Ben", "Caroline", "Dave", "Esther"]
        gradesAlice = [4, 2, 4, 5, 6, 6]
        gradesBen = [5, 1, 2, 4, 4, 3]
        gradesCaroline = [4, 5, 5, 2, 3, 4]
        gradesDave = [1, 2, 3, 4, 5, 6]
        gradesEsther = [6 , 5, 6, 4, 3, 5]
        allgrades = [gradesAlice, gradesBen, gradesCaroline, gradesDave, gradesEsther]

        for i in range(len(mylist)):
            print(mylist[i] + " has an average grade of")
            print(g.average(allgrades[i]))

    def average(self, list):
        total = 0
        size = 0
        for element in list:
            size += 1
            total += element
            
        return (round(total / size, 3))
    

g = grade()
g.main()
