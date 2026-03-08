class StudentMarks:
    def __init__(self, marks):
        self.marks = marks

    def last_three_avg(self):
        try:
            if len(self.marks) < 3:
                raise Exception
            avg = sum(self.marks[-3:]) / 3
            print("Average of last 3 marks is:", avg)
        except:
            print("Not enough marks to calculate average")


marks = [50, 60, 70, 80, 90]

student = StudentMarks(marks)
student.last_three_avg()