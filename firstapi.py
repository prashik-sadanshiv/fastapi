from fastapi import FastAPI
from typing import Optional
from  pydantic import BaseModel


# Kartik 

app = FastAPI()

students = {
  1 : {
    "name": "Latika",
    "age" : 27,
    "city" : "akoal"
  }
}

class Student(BaseModel):
  Name : str
  age : int
  city : str


class UpdateStudent(BaseModel):
  name :Optional[str] = None
  age :Optional[int] = None
  city :Optional[str] = None
  
  
@app.get("/get-student")
def get_student(student_id:int):
  return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(name:str):
  for student_id in students:
    if students[student_id]["name"] == name:
      return students[student_id]
  return "Data Not Found"

@app.post("/create-student/{student_id}")
def create_student(student_id:int, student:Student):
  if student_id in students:
    return "Student already present"
  
  students[student_id] = student
  return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id:int, student:UpdateStudent):
  
  if student_id not in students:
    return "Data is not present"
  
  students[student_id] = student
  return students[student_id]
