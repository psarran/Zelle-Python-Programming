# zelle 10.4 text exercise - best student

## program reads in a file of students and finds the one with best gpa

class Student:

    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints / self.hours

def makeStudent(infoStr):

    name, hours, qpoints = infoStr.split('\t')
    s = Student(name, hours, qpoints)
    return s

def main():

    filename = input('name of file with student data: ')
    infile = open(filename, 'r')

    best = []
    best.append(makeStudent(infile.readline()))

    for line in infile:
        s = makeStudent(line)

        if s.gpa() == best[0].gpa():
            best.append(s)
        elif s.gpa() > best[0].gpa():
            best = []
            best.append(s)

    infile.close()

    print('Best students are: \n')

    for i in best:
        print(i.getName(), ' {0:0.2f}'.format(i.gpa()))

main()    
#if __name__ == '__main__': main()
