import school

a = school.Student("kim", 3)
b = school.Student("pack", 2)
c = school.Student("jung", 1)
mathTeacher = school.Teacher("lee", "수학")
ban1 = school.Class(1, mathTeacher)

ban1.addStudent(a)
ban1.addStudent(b)
ban1.addStudent(c)
ban1.introducing()
ban1.mathavg()
a.studyMath()
a.studyMath()
ban1.mathavg()