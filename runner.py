from classes.school import School

school = School('Ridgemont High')

mode = ""
while mode != "5":
    mode = input("\nWhat would you like to do?\n\nOptions:\n\t1. List All Students\n\t2. View Individual Student <student_id>\n\t3. Add a Student\n\t4. Remove a Student <student_id>\n\t5. Quit\n")

    if mode == '1':
        school.list_students()
    elif mode == '2':
        student_id = input('Enter student id:')
        student = school.find_student_by_id(student_id)
        print(str(student))
    else:
        pass