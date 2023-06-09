from new_student import Student

student = Student(name="Edward", surname="agle")
print(student)

try:
    student_id = Student(name="Edward", surname="agle", id="efw")
    print("Error: should raise an error")
except TypeError:
    print("error catched successfuly")
