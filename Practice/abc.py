def create_stud(name:str,age:int,college:str):
    if type(name)== str and type(age)== int and type(college)== str:
        print(name)
        print(age)
        print(college)
        print("Student data created")   
    
    else:
        raise TypeError("invalid type of Input.")

create_stud('Krishna','22','ycce')