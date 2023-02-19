import school

a = school.Student("kim", 3)
mathTeacher = school.Teacher("lee", "수학")
ban1 = school.Class(1, mathTeacher)

ban1.introducing()
ban1.addStudent(a)
ban1.introducing()