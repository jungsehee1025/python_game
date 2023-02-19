import school

a = school.Student("kim", 3)
b = school.Student("lee", 2)
c = school.Student("back", 2)

a.greeting()
b.greeting()
c.greeting()


mathTeacher = school.Teacher("kim", "수학")
engTeacher = school.Teacher("lee", "영어")

mathTeacher.greeting()
engTeacher.greeting()