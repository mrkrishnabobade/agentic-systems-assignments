from fastapi import FastAPI, HTTPException, Query
import json
app= FastAPI()


# localhost:8000/hello
@app.get("/hello")
def say_hello():
    return "Hello World"

#localhost:8000/bye
@app.get("/bye")
def say_bye():
    return "Bye Everyone"

#Loading students Data
def load_stud_data():
    with open('students.json','r') as f:
        students_data= json.load(f)
    return students_data

# Get all the students
"""
@app.get("/students")
def get_all_students(student_id:str = Query(None)):
    data=load_stud_data()
    if student_id:
        if student_id in data:
            return data[student_id]
        return {"error":"not found"}
    return data
""" 

@app.get("/students/{students_id}")
def get_stud_id(students_id:str):
    Student=load_stud_data()

    if students_id not in Student:
        raise HTTPException(status_code= 404,detail= "Student not found" )
    return Student[students_id]
