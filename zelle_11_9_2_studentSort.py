#zelle 11.9.2 studetSort

""" Program to import student grade data, sort on GPA, name, or # of credits,
    then output the file. Default sort key is name.
"""

from zelle_10_4_text_exercise_student_grades import Student, makeStudent

def getInputs():
    """ gather the input and output file names and sort key.
        also sets default file names if none are entered
    """
    infilename = input('name of file w student data: ')
    if infilename == "":
        infilename = 'zelle 10.4 student grades.txt'
    outfilename = input('name of file to write sorted data to: ')
    if outfilename == "":
        outfilename = 'zelle 11.9.2 student sort.txt'
    sortkey = input("sort key - 'gpa' 'name' or 'credits': ")
    outfile = open(outfilename, 'w')
    return infilename, outfilename, sortkey

def readStudents(infilename):
    """ given the file name, import the data and create a list of student objects
    """
    infile = open(infilename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, outfilename):
    """ write the student objects to given file as tab separated list
    """
    outfile = open(outfilename, 'w')
    for s in students:
        print('{0}\t{1}\t{2}'.
            format(s.getName(), s.getHours(), s.getQPoints()),
            file=outfile)
    outfile.close()

def sortStudents(students, sortkey):
    """ sort the list of student objects on the given key
        default sort is name if none or invalid key is given
    """
    if sortkey == 'gpa':
        students.sort(key=Student.gpa)
    elif sortkey == 'credits':
        students.sort(key=Student.getQPoints)
    else:
        students.sort(key=Student.getName)
    return students

def main():
    infilename, outfilename, sortkey = getInputs()
    students = readStudents(infilename)
    students = sortStudents(students, sortkey)
    writeStudents(students, outfilename)
    
if __name__ == '__main__': main()
    
