from StudentProfile import *
from TeacherProfile import *

def studnets():
    s1 = studentprofile("","",0,0,"",0.00,"",0,0,0)
    s1.f_name,s1.l_name,s1.age,s1.phone,s1.address = input().split(",")
    s1.cgpa,s1.attendance,s1.total_marks = input().split(",")
    print(s1.full_name())
    print(s1.complete_proinfo())
    print(s1.normal_details())
    print(s1.cpga_info())
    print(s1.other_info())

def teachers():
    t1 = teacherprofile("","",0,0,"",0,0)
    t1.f_name,t1.l_name,t1.age,t1.phone,t1.address = input().split(",")
    t1.attendance,t1.payAbleAmount = input().split(",")
    print(t1.other_info())
    print(t1.teachersPaymentInfo())

if __name__ == '__main__':
    print("1. Update Student's profile")
    print("2. Update Teacher's profile")
    if int(input()) == 1:
        studnets()
    else:
        teachers()