from fastapi import FastAPI, Path
from typing import Optional
app = FastAPI()


# ------------------
#basic page 
# ------------------
@app.get('/')
def index():
    return {"name":"Shan"}


# ------------------
#path parameter 
# ------------------
students_dict = {
    1: {
        "name": "shan",
        "age": 25,
        "year": 12
    }
}

# Note: The path parameter name in the URL ({student_id}) must exactly match the function argument (student_id)
# for FastAPI to map the value correctly. If the names differ, the OpenAPI docs may still show the endpoint,
# but actual requests using the URL will not work as expected.@app.get('/get-student/{student_id}')
@app.get('/get-student/{student_id}')
def get_student(student_id:int = Path(None, description='The ID of student you want to view', gt=0, lt=3)):
    return students_dict[student_id]

#Path(is a utility from FastAPI) function to declare metadata and validation for a path parameter.
#default values, description-> metadata used in docs(swagger ui)


# ------------------
#querry parameters 
# ------------------
@app.get('/get-by-name')
def get_student(*, name:Optional[str] = None,  test:int): 
    #can also write def get_student(name:str = None):  #name is no longer compulsary 
    #python doesnt allow optional argument before required argument, to solve it we can rearange args or just add * in start 
    #parameter may be a string or may be None
    # * means: All parameters after the * must be passed as keyword arguments (not positional).
    #so even if we have non-default argument following default argument, it works and python doesnt show error (because Keyword-Only Parameters Don't Follow That Rule)
    for x,y in students_dict.items():
        if y['name']==name:
            return y
    return {"Data": "Not Found"}


# ------------------
#combining path and querry parameters 
# ------------------
@app.get('/get-by-name/{student_id}')
def get_student(*, student_id:int, name:Optional[str] = None,  test:int): 
    print(f"got paras: student_id[{student_id}],  name:[{name}], test:[{test}]")
    for x,y in students_dict.items():
        if y['name']==name:
            return y
    return {"Data": "Not Found"}


# ------------------
#request body and post method  - create 
# ------------------
from pydantic import BaseModel 

#fastApi uses pydantic for validatoin under the hood
#it does type coercion(a form of type casting)
class Student(BaseModel):
    name : str
    age : int 
    year : str

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student_detials: Student):
    if student_id in students_dict:
        return {"Error":"student exist"}
    students_dict[student_id] = student_detials
    return students_dict[student_id]



# ------------------
#put method - update
# ------------------ 
class Student2(BaseModel):
    name : Optional[str]=None
    age : Optional[int]=None 
    year : Optional[str]=None
#new class because if someone want to update a value in Student he have to give all the paramentres of student 
#which is not a good practive

@app.put('/update-student/{student_id}')
def update_student(student_id: int, student: Student2):
    if(student_id not in students_dict):
        return {"Error":"Student does not exist"}

    temp_dict = students_dict[student_id]

    if student.name is not None:
        temp_dict["name"] = student.name
    if student.age is not None:
        temp_dict["age"] = student.age
    if student.year is not None:
        temp_dict["year"] = student.year


    students_dict[student_id] = temp_dict
    return temp_dict
    


# ------------------
#delete method 
# ------------------
@app.delete('/delete-student/{student_id}')
def delete_student(student_id: int):
    if student_id not in students_dict: 
        return {"error": "Student does not exist"}
    
    del students_dict[student_id]
    return {"messgae":"delete success"}