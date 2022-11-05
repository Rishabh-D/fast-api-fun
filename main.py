from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

students = {
  "1": {
    "name": "rishabh",
    "age": 17,
    "year": "year 12"
  }
}

class Student(BaseModel):
  name: str
  age: int
  year: str 

class UpdateStudent(BaseModel):
  name: Optional[str] = None
  age: Optional[str] = None
  year: Optional[str] = None


@app.get("/")
def index():
  return {"name": "Rishabh"}

# path parameter
@app.get("/student/{student_id}")
def get_student(student_id: int = Path(None, description="this is just a description", gt=0, lt=4)):
  return students[student_id]

#query parameter
@app.get("/studentByQuery")
def get_student(name: str, light: str):
  print(name, light)
  for student in students:
    if students[student]["name"] == name:
      return students[student]

# path and query parameter combined
@app.get("/studentByPathAndQuery/{id}")
def get_student(name: str, light: str):
  print(name, light)
  for student in students:
    if students[student]["name"] == name:
      return students[student]

# Request body and the post metod
@app.post("/create-student/{student-id}")
def create_student(student_id : int, student: Student):
  if student_id in students:
    return {"error": "Student already exists"}
  students[student_id] = student
  return students[student_id]
  

# request body and the put method
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
  if student_id not in students:
    return {"error": "this record does not exists"}
  for key in student: 
    students[student_id][key] = student[key]
  return students[student_id]

# delete method
@app.delete("/delete-student/{student_id}")
def delete_student(student_id : str):
  if student_id not in students:
    return {"error":"no such record exists"}
  del students[student_id]
  return {"message": "deleted successfully"}
